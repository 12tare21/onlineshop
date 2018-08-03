from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from products.models import Product

def userpage(request,user_slug):
    profile_object=get_object_or_404(Profile,slug=user_slug)
    products=Product.objects.filter(profile=profile_object)
    content={
        'profile':profile_object,
        'products':products,
    }
    return render(request,'accounts/user.html',content)
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords do not match. '})
    else:
        return render(request,'accounts/signup.html',{})        
    

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or password are incorrect. '})
    else:
        return render(request,'accounts/login.html',{})
@login_required
def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('home')
    