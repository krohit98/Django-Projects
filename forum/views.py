from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from userProfile.models import userPosts, comments

# Create your views here.
def index(request):
    allPosts=userPosts.objects.all().order_by('-pk')
    allComments=comments.objects.all().order_by('-pk')
    return render(request, 'index.html',{'allPosts':allPosts,'allComments':allComments})

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('userProfile/profile')
        else:
            messages.info(request,'Enter valid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')