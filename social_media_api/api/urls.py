from django.urls import path
from .views import (
    RegisterView,
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
    LikeView,
    FollowView,
    UserListView,
    UserDetailView,
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),

    # Posts
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Comments
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    # Likes
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='like'),

    # Follow
    path('users/<int:user_id>/follow/', FollowView.as_view(), name='follow'),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]