from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    comment_id = serializers.CharField(max_length=20)
    comment = serializers.CharField(default="")
    article = serializers.CharField(default="")
    thumbs_up = serializers.IntegerField(default=0)
    thumbs_down = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
