from django.contrib import admin
from django.urls import path
from django.urls import path, include

from insta.views import HomeView, ArticleDetailView , AddPostView , UpdatePostView



urlpatterns = [
    path('' , HomeView.as_view() , name="home"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    # path('about/' ,views.about , name='blog-about')

]
