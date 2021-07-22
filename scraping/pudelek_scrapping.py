import requests
from bs4 import BeautifulSoup
import os
import sys
import json
import re
from Article import Article
from Comment import Comment
from datetime import datetime


def get_pudelek_articles():
    pudelek_articles = list()
    comments_list = list()
    now = datetime.now()

    url = "https://www.pudelek.pl/"
    result = requests.get(url)

    res = result.content
    soup = BeautifulSoup(res, "html.parser")
    mydivs = soup.findAll(
        "div", {"data-st-area": re.compile("main-stream-[0-9]*")})

    for div in mydivs:

        articleUrl = "https://pudelek.pl" + div.find('a')['href']
        title = div.find('a')['title']

        article = Article(title, articleUrl, now)
        pudelek_articles.append(article)

    for article in pudelek_articles:
        result = requests.get(article.url)

        res = result.content
        soup = BeautifulSoup(res, "html.parser")
        mydivs = soup.findAll(
            "div", {"class": re.compile("kvmdow.*")})

        for div in mydivs:

            button_up = div.find("button", {"data-st-area": "comment-up"})

            if button_up is not None:
                up_counter = button_up.find(
                    ("div", {"class": re.compile(".*fJEayh")}))
                if up_counter is not None:
                    up_counter = up_counter.text

            button_down = div.find("button", {"data-st-area": "comment-down"})

            if button_down is not None:
                down_counter = button_down.find(
                    ("div", {"class": re.compile(".*fJEayh")}))
                if down_counter is not None:
                    down_counter = down_counter.text

            comment = div.find("div", {"class": re.compile(".*LsrOO$")})

            if comment is not None:
                comment = comment.text

            comment_item = Comment(
                article.title, comment, up_counter, down_counter)
            comment_item.print_comment()
            comments_list.append(comment_item)
    return comments_list


def save_comments(api_url, comments_list):
    payload = '{"comments": ['
    for comment in comments_list:
        json_string = json.dumps(comment.__dict__, sort_keys=True,
                                 indent=2, ensure_ascii=True)
        payload = payload + json_string + ","

    payload = payload[:-1] + "]}"

    headers = {'Content-Type': 'application/json'}

    print(payload)
    response = requests.request("PUT", api_url, headers=headers, data=payload)
    print(response.status_code)


def main():
    api_url = "http://127.0.0.1:8000/api/comment"
    comments = get_pudelek_articles()
    save_comments(api_url, comments)


if __name__ == "__main__":
    main()
