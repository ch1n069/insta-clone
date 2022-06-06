from django.contrib import admin
from django.urls import path
from django.urls import path, include

from insta.views import HomeView



urlpatterns = [
    path('' , HomeView.as_view() , name="home"),
    # path('about/' ,views.about , name='blog-about')

]
