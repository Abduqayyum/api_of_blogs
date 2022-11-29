from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Category
        fields = ['id', 'name', "posts", "owner"]


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    owner = serializers.ReadOnlyField(source="owner.username")
    comments = serializers.StringRelatedField(many=True, read_only=True)
    # categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "body", "owner", "comments", "categories", "image"]

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id","username","posts", "posts","comments","categories"]

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


