from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Profile
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.exceptions import PermissionDenied

# search products
def search(request):
    # get search input named 'q'
    search_query = request.GET.get('q')
    # check if anything entered in 'q'
    if search_query:
        # get list of products which title contains 'q' input
        product_list=Product.objects.filter(title__icontains=search_query).order_by('-pub_date')
        paginator=Paginator(product_list,9)
        page=request.GET.get('page')
        products=paginator.get_page(page)
        content={
            'products':products,
            'search_input':search_query
        }
        return render(request,'products/search.html',content)
    return redirect('home')
    # need some javascript to stay on page if search_query is empty
    # instead redirecting home

#homepage
def home(request):
    categories=Category.objects.all()
    products_all=Product.objects.all()
    products=[]
    # get max 3 Product objects of every category and save them in products list
    for category in categories: 
        count=0
        for product in products_all:
            if product.category==category:
                products.append(product)
                count+=1
            if count>2:
                break
    content={
        'products':products,
        'categories':categories,
    }
    return render(request,'products/index.html',content)

# product detail page    
def detail(request,product_id,slug):
    # get specific product based on slug and id
    product = get_object_or_404(Product,slug=slug,pk=product_id)
    content={
        'product':product
    }
    return render(request,'products/detail.html',content)

# get category page    
def category(request,slug):
    # get category and all related objects to it
    category=get_object_or_404(Category,slug=slug)
    product_list=Product.objects.filter(category=category)
    paginator = Paginator(product_list,9)
    page = request.GET.get('page')
    products=paginator.get_page(page)
    content={
        'category':category,
        'products':products
    }
    return render(request,'products/category.html',content)

#create new product
@login_required
def create(request):
    categories=Category.objects.all()
    content={
        'categories':categories
    }
    # check if request is POST or GET
    if request.method=='POST':
        # check if inputs are missing or incorrect
        if not request.POST.get('title'):
            return render(request,'products/create.html',{'categories':categories,'error':'Title is missing.'})
        if not request.POST.get('price') :
            return render(request,'products/create.html',{'categories':categories,'error':'Price is missing.'})
        try:
            price=int(request.POST.get('price'))
        except ValueError:
            return render(request,'products/create.html',{'categories':categories,'error':'Price is not entered correctly.'})
        if not request.POST.get('description'):
            return render(request,'products/create.html',{'categories':categories,'error':'Description is missing.'})
        if not request.FILES.get('image'):
            return render(request,'products/create.html',{'categories':categories,'error':'Image is missing.'})
        else:
            product = Product()
            product.title = request.POST.get('title')
            product.slug = slugify(request.POST.get('title'))
            product.price = int(request.POST.get('price'))
            product.description = request.POST.get('description')
            category_list=Category.objects.filter(name=request.POST.get('categories'))
            product.category =  category_list[0]
            # get queryset because based on select category names
            # and adding first from queryset because it is only one
            product.image = request.FILES.get('image')
            product.pub_date = timezone.datetime.now()
            profile_list = Profile.objects.filter(user=request.user)
            product.profile = profile_list[0] 
            product.save()
            return render(request,'products/create.html',content)
    else:
        return render(request,'products/create.html',content)
@login_required
def update(request,product_id,slug):
    profile=get_object_or_404(Profile,user=request.user)
    product =Product.objects.get(pk=product_id)
    # raise PermissionDenied if loged profile is not product's profile
    if product.profile != profile:
        raise PermissionDenied
    categories=Category.objects.all()
    content={
        'product':product,
        'categories':categories,
    }
    # check if request is POST or GET
    if request.method=='POST':
        product.title=request.POST.get('title')
        product.slug=slugify(request.POST.get('title'))
        product.price=request.POST.get('price')
        category_list=Category.objects.filter(name=request.POST.get('categories'))
        product.category=category_list[0]
        product.description=request.POST.get('description')
        if request.FILES.get('image'):
            product.image=request.FILES.get('image')
        product.save()
        content['changed']='Your changes have been saved.'
        return render(request,'products/detail.html',content)
    else:
        return render(request,'products/update.html',content)

# delete your product
@login_required
def delete(request,slug,product_id):
    product=Product.objects.get(pk=product_id)
    # raise PermissionDenied if loged user is not product's user
    if product.profile.user != request.user:
        raise PermissionDenied
    product.delete()
    return redirect('home')