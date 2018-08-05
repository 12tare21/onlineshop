from .models import Category,Product
from datetime import date
from django.shortcuts import render

def add_category_to_context(request):
    categories=Category.objects.all()
    return{'categories':categories,}
def add_year_to_context(request):
    year = date.today().year
    return{'year':year}
