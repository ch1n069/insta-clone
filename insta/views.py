from django.shortcuts import render
from django.http import HttpResponse
from insta.models import Post 
from django.views.generic import ListView , DetailView
# Create your views here.



class HomeView (ListView):
    model = Post

    template_name = 'insta/home.html'


class ArticleDetailView (DetailView):

    model = Post

    template_name = "insta/post_details.html"

