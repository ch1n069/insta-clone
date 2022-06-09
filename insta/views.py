from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect 
from insta.models import Post
from django.urls import reverse_lazy, reverse
from insta.forms import PostForm , UpdateForm
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
# Create your views here.



def LikeView(request, pk):
    post =  get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(request, 'home')
    




class HomeView (ListView):
    model = Post

    template_name = 'insta/home.html'
    ordering = ['-post_date']
    
    # ordering by id but conventional way is to use data 
    # def get(self, request):
    #     posts = Post.object.order_by('-post_date')[:15]
    #     ctx = {
    #         'objects_list':posts
    #     }
    #     return render(request, 'insta/home.html', ctx)


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
    



class UserPostView(ListView):

    model = Post
    
  
    template_name = "insta/users_posts.html"
    ctx = {}

    def get_queryset(self):
       
        return Post.objects.filter(author=self.kwargs['pk'])