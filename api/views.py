from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from api.permissions import IsAuthorOrReadOnly
from news_portal.models import Author
from api.serializers import PostSerializer, Post

class NewsViewSet(viewsets.ModelViewSet):
    content = 'NW'
    queryset = Post.objects.filter(content_type=content)
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        try:
            author = Author.objects.get(user=self.request.user)
            serializer.save(posted_by=author, content_type=self.content)
        except Author.DoesNotExist:
            raise ValidationError("Access denied. You're not an author.")

class ArticlesViewSet(viewsets.ModelViewSet):
    content = 'AT'
    queryset = Post.objects.filter(content_type=content)
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        try:
            author = Author.objects.get(user=self.request.user)
            serializer.save(posted_by=author, content_type=self.content)
        except Author.DoesNotExist:
            raise ValidationError("Access denied. You're not an author.")
