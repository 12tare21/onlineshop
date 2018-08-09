from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from products.models import Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# change profile settings
@login_required
def settings(request):
    user=request.user
    profile=Profile.objects.filter(user=user)
    content = {
        'profile':profile[0],
    }
    # check if request is POST or GET
    if request.method=='POST':
        user=User.objects.filter(username=request.user.username)
        # need to filter because updating email field which is in User model
        user.update(email=request.POST.get('email'))
        # updating profile fields with inputs in form
        profile.update(address=request.POST.get('address'))
        profile.update(city=request.POST.get('city'))
        profile.update(country=request.POST.get('country'))
        profile.update(bio=request.POST.get('bio'))
        return redirect('profilepage')
    else:
        return render(request,"accounts/yoursettings.html",content) 

# view your profile
@login_required
def yourprofile(request):
    user=request.user
    # get Profile object of loged in user
    profile=Profile.objects.filter(user=user)
    # get Product objects associated with profile
    product_list=Product.objects.filter(profile=profile[0])
    paginator=Paginator(product_list,9)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    content={
        'profile':profile[0],
        'products':products
    }
    return render(request,'accounts/yourprofile.html',content)

# view someone's profile
def userpage(request,user_slug):
    profile_object=get_object_or_404(Profile,slug=user_slug)
    # check if profile_object user is loged user 
    # and if redirect to your profile page
    if profile_object.user==request.user:
        return redirect('profilepage')
    product_list=Product.objects.filter(profile=profile_object)
    paginator=Paginator(product_list,9)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    content={
        'profile':profile_object,
        'products':products,
    }
    return render(request,'accounts/user.html',content)


def signup(request):
    # check if request is POST or GET
    if request.method=='POST':
        #check if all fields are entered correctly and user is not already registered
        if not request.POST.get('email'):
            return render(request,'accounts/signup.html',{'error':'E-mail must be entered. '})
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
    # check if request is POST or GET
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
@login_required
def password_change(request):
    if request.method=='POST':
        #check if old password is correct
        if not request.user.check_password( request.POST.get('old')):
            return render (request,'accounts/change-password.html',{'error':'You entered incorrect password.'})
        #check if passwords match
        if request.POST.get('password1') != request.POST.get('password2'):
            return render (request,'accounts/change-password.html',{'error':'Passwords do not match.'})
        request.user.set_password(request.POST.get('password1'))
        user=request.user
        request.user.save()
        auth.login(request,user)
        return render (request,'accounts/change-password.html',{'error':'Password has been changed.'})
    else:
        return render (request,'accounts/change-password.html',{})
        
#delete your profile and products added by your proifle
@login_required
def delete(request):
    profile=Profile.objects.get(user=request.user)
    products=Product.objects.filter(profile=profile)
    for product in products:
        product.delete()
    profile.user.delete()
    profile.delete()
    return redirect('home')