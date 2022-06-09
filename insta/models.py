from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.


class HashTag(models.Model):
    name = models.CharField(max_length=100 , default='instaperfect')


    def __str__(self):
        return self.name 


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    title_tag = models.CharField(max_length=100,)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="post")
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    hash_tag = models.CharField(max_length=100, default="instaperfect")
    likes = models.ManyToManyField(User, related_name="insta_post")
    image = models.ImageField(null = True, blank=True,  upload_to="images")



    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
