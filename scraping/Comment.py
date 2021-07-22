class Comment:
    def __init__(self, title, comment, up, down):
        self.title = title
        self.comment = comment
        self.thumbs_up = up
        self.thumbs_down = down

    def print_comment(self):
        print(self.title)
        print(self.comment)
        print(self.thumbs_up + " UP")
        print(self.thumbs_down + " DOWN")
