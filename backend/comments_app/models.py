from django.db import models


class Comment(models.Model):
    comment = models.TextField(default="")
    title = models.TextField(default="")
    thumbs_up = models.TextField(default=0)
    thumbs_down = models.TextField(default=0)

    # start_dttm = models.DateTimeField(
    #     default=timezone.now)
    # end_dttm = models.DateTimeField(default=timezone.now)

    def add_comment(self):
        # self.start_dttm = timezone.now()
        self.save()

    def __str__(self):
        return self.comment


class Article(models.Model):
    title = models.TextField(default="")
    url = models.TextField(default="")
    date = models.TextField(default="")
