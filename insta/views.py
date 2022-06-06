from django.shortcuts import render
from django.http import HttpResponse
from insta.models import Post
from insta.forms import PostForm 
from django.views.generic import ListView , DetailView , CreateView , UpdateView
# Create your views here.



class HomeView (ListView):
    model = Post

    template_name = 'insta/home.html'


# shows one post
class ArticleDetailView (DetailView):

    model = Post

    template_name = "insta/post_details.html"

# create a post 
class AddPostView(CreateView):

    model = Post
    form_class = PostForm
    template_name = "insta/add_post.html"
    # fields = ('title' ,'title_tag', 'body')




# update view 

class UpdatePostView(UpdateView):

    model = Post

    fields = ['title', 'title_tag','body']

    template_name = "insta/update_post.html"
    
