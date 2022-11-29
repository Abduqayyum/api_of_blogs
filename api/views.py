from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, User, Post, PostSerializer, Comment, CommentSerializer, Category, CategorySerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




    