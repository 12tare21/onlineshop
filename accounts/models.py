from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

# Extended user model with slug, image, location fields, bio
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=250,blank=True)
    address=models.CharField(max_length=250,blank=True)
    city=models.CharField(max_length=250,blank=True)
    country=models.CharField(max_length=250,blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

# create_profile - function used to create Profile object and slug
# and associating it with User object if user object is created
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_slug=slugify(kwargs['instance'].username)
        profile=Profile.objects.create(user=kwargs['instance'],slug=user_slug)
# post_save - connect create_profile with User 
post_save.connect(create_profile,sender=User)
