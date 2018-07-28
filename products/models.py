from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    pub_date=models.DateField(auto_now=False)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def pub_date_preety(self):
        return self.pub_date.strftime('%d/%m/%Y')
    def __str__(self):
        return self.title
