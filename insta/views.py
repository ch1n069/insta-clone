from django.shortcuts import render
from django.http import HttpResponse
from insta.models import Post
from django.urls import reverse_lazy
from insta.forms import PostForm , UpdateForm
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
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
    form_class = UpdateForm

    # fields = ['title', 'title_tag','body']

    template_name = "insta/update_post.html"
    

class DeletePostView(DeleteView):
    model = Post

    # fields = ['title', 'title_tag','body']

    template_name = "insta/delete_post.html"
    success_url = reverse_lazy('home')
    
