from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , DetailView
# Create your views here.



def home(request):


    return render(request , 'insta/home.html')




def about(request):


    return render(request , 'insta/about.html')
