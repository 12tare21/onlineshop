from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.db.models.signals import pre_init,post_init
from django.template.defaultfilters import slugify

# Category model
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
# create slug after create category or change of category's name
def create_category_slug(**kwargs):
    instance=kwargs['instance']
    category_slug=slugify(instance.name)
    instance.slug=category_slug

# post_init executes after creating Category object
post_init.connect(create_category_slug,Category)

# Product model
class Product(models.Model):    
    title=models.CharField(max_length=250)
    price=models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date=models.DateField(auto_now=False)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    def pub_date_preety(self):
        return self.pub_date.strftime('%d/%m/%Y')
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-pub_date',)
        verbose_name = 'product'
        verbose_name_plural='products'

# create_product_slug - create slug after creating product or changing product's name
def create_product_slug(**kwargs):
    instance = kwargs['instance']
    product_slug=slugify(instance.title)
    instance.slug=product_slug
    
# executes after creating Product object    
post_init.connect(create_product_slug,Product)
