from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("posts/", views.PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("comments/", views.CommentList.as_view(), name="comment-list"),
    path("comments/<int:pk>/", views.CommentDetail.as_view(), name="comment-detail"),
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path("categories/<int:pk>/", views.CategorDetail.as_view(), name="categories-detail")
]
