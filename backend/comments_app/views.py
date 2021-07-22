from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, View
from .serializers import CommentSerializer
from .models import Comment


class CommentView(APIView):

    def post(self, request):

        comment = request.data.get('comment')
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()

        return Response({"success": "Comment '{}' created successfully".format(comment_saved.id)})

    def get(self, request):

        comment_id = request.GET.get('comment_id')

        if comment_id is None:
            comments = Comment.objects.all()
        else:
            comments = Comment.objects.filter(
                comment_id=comment_id)
        serializer = CommentSerializer(comments, many=True)

        return Response({"comments": serializer.data})

    def put(self, request):
        comments = request.data.get('comments')
        comments_list = list()

        for comment in comments:
            print(comment)
            serializer = CommentSerializer(data=comment)

            if serializer.is_valid(raise_exception=True):
                comment_saved = serializer.save()
                comments_list.append(comment)

        return Response({"comments_list": comments_list})
