from django.db import models
import datetime

# Create your models here.
class userPosts(models.Model):
    name=models.CharField(max_length=50)
    topic=models.CharField(max_length=100)
    post=models.TextField()
    date=models.DateTimeField(auto_now_add=True, blank=True)

class comments(models.Model):
    topic=models.ForeignKey(userPosts,on_delete=models.CASCADE)
    comments=models.TextField()
    name=models.CharField(max_length=50, blank=True)