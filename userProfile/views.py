from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import userPosts, comments

# Create your views here.
def profile(request):
    myPosts=userPosts.objects.filter(name=request.user.username).order_by('-pk')
    allComments=comments.objects.all().order_by('-pk')
    return render(request,'profile.html',{'myPosts':myPosts, 'allComments':allComments})

def logout(request):
    auth.logout(request)
    return redirect('/')

def createPost(request):
    post=request.POST['newPost']
    topic=request.POST['newTopic']
    userP=userPosts()
    userP.name=request.user.username
    userP.topic=topic
    userP.post=post
    userP.save()
    return redirect('profile')

def deletePost(request):
    topicId=request.POST['delTopicId']
    post=userPosts.objects.get(pk=topicId)
    post.delete()
    return redirect('profile')
    
def postComment(request):
    tid=request.POST['topic-id']
    newComment=request.POST['comment']
    comm=comments()
    comm.topic_id=tid
    comm.comments=newComment
    comm.name=request.user.username
    comm.save()
    return redirect(request.META.get('HTTP_REFERER'))

def deleteComment(request,commentId):
    deleteId=commentId
    comm=comments.objects.get(pk=deleteId)
    comm.delete()
    return redirect(request.META.get('HTTP_REFERER'))