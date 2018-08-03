from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=250,blank=True)
    location = models.CharField(max_length=250,blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.user.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_slug=slugify(kwargs['instance'].username)
        profile=Profile.objects.create(user=kwargs['instance'],slug=user_slug)

post_save.connect(create_profile,sender=User)
