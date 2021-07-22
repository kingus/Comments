class Comment:
    def __init__(self, title, comment, up, down):
        self.title = title
        self.comment = comment
        self.up = up
        self.down = down

    def print_comment(self):
        print(self.title)
        print(self.comment)
        print(self.up + " UP")
        print(self.down + " DOWN")
