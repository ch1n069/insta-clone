from django.contrib import admin
from django.urls import path
from django.urls import path, include

from insta.views import HomeView, ArticleDetailView



urlpatterns = [
    path('' , HomeView.as_view() , name="home"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name="post-detail")
    # path('about/' ,views.about , name='blog-about')

]
