from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Profile
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def search(request):
    search_query = request.GET.get('q')
    if search_query:
        product_list=Product.objects.filter(title__icontains=search_query).order_by('-pub_date')
        paginator=Paginator(product_list,9)
        page=request.GET.get('page')
        products=paginator.get_page(page)
        return render(request,'products/search.html',{'products':products,'search_input':search_query})
    return redirect('home')
    #need some javascript to stay on page if search_query is empty instead redirect home
def home(request):
    return render(request,'products/index.html',{})
def detail(request,product_id,slug):
    product = get_object_or_404(Product,slug=slug,pk=product_id)
    return render(request,'products/detail.html',{'product':product})
def category(request,slug):
    category=get_object_or_404(Category,slug=slug)
    product_list=Product.objects.filter(category=category)
    paginator = Paginator(product_list,9)
    page = request.GET.get('page')
    products=paginator.get_page(page)
    return render(request,'products/category.html',{'category':category,'products':products})

@login_required
def create(request):
    categories=Category.objects.all()
    if request.method=='POST':
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
            category_list=list(Category.objects.filter(name=request.POST.get('categories')))
            print(category_list)
            product.category =  category_list[0]
            # convert to list because error,from list used one object,because
            # filter returns queryset
            product.image = request.FILES.get('image')
            product.pub_date = timezone.datetime.now()
            profile_list = list(Profile.objects.filter(user=request.user))
            product.profile = profile_list[0] 
            product.save()
            return render(request,'products/create.html',{'categories':categories})
    else:
        return render(request,'products/create.html',{'categories':categories})