from django.shortcuts import render
from django.http import HttpResponse
from insta.models import Post
from insta.forms import PostForm 
from django.views.generic import ListView , DetailView , CreateView
# Create your views here.



class HomeView (ListView):
    model = Post

    template_name = 'insta/home.html'


class ArticleDetailView (DetailView):

    model = Post

    template_name = "insta/post_details.html"



class AddPostView(CreateView):

    model = Post
    form_class = 
    template_name = "insta/add_post.html"
    fields = ('title' ,'title_tag', 'body')