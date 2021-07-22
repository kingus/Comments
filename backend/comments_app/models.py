from django.db import models


class Comment(models.Model):
    comment_id = models.TextField(default="", unique=True)
    comment = models.TextField(default="")
    article = models.TextField(default="")
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

    # start_dttm = models.DateTimeField(
    #     default=timezone.now)
    # end_dttm = models.DateTimeField(default=timezone.now)

    def add_comment(self):
        # self.start_dttm = timezone.now()
        self.save()

    def __str__(self):
        return self.comment
