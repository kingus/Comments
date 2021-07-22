from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include
from comments_app.views import CommentView

urlpatterns = [
    path('comment', CommentView.as_view()),

]
