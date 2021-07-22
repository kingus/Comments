from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    comment = serializers.CharField(default="")
    title = serializers.CharField(default="")
    thumbs_up = serializers.IntegerField(default=0)
    thumbs_down = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
