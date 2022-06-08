from django.contrib import admin
from django.urls import path
from django.urls import path, include

from insta.views import HomeView, ArticleDetailView , AddPostView , UpdatePostView , DeletePostView , LikeView



urlpatterns = [
    path('' , HomeView.as_view() , name="home"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('delete_post/edit/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name='like_post')

    # path('about/' ,views.about , name='blog-about')

]
