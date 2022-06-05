from django.contrib import admin
from django.urls import path
from insta import views



urlpatterns = [
    path('' ,views.index , name='index')
]
