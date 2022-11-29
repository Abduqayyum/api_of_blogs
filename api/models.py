from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to="image", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.body

class Category(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories", default="")
    posts = models.ManyToManyField(Post, related_name="categories", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories" 
        ordering = ["-created_at"]

    def __str__(self):
        return self.name