from django.contrib import admin
from django.urls import path
from django.urls import path, include

from insta import views



urlpatterns = [
    path('' ,views.home , name='home')
]
