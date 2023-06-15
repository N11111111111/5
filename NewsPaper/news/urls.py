from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('news/', PostList.as_view(), name='posts'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchPosts.as_view(), name='post_search'),
    path('news/add/', PostCreateView.as_view(), name='post_create'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),



]










