from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import UserRegisterView




urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),


  
    # path('about/' ,views.about , name='blog-about')

]
