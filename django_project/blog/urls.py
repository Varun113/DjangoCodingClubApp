from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostHintView,
    feedback,
    submit,
    search,
    surprise
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('results', search, name='qsns-search'),
    path('feedback', feedback, name='feedback'),
    path('surprise', surprise, name='surprise'),
    path('submit', submit, name='submit'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/hint', PostHintView.as_view(), name='post-hint'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
