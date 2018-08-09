from .models import Category,Product
from datetime import date
from django.shortcuts import render

# add_category_to_context - need to add list of categories in base.html
def add_category_to_context(request):
    categories=Category.objects.all()
    return{'categories':categories,}

#add_year_to_context - need to add current year in footer
def add_year_to_context(request):
    year = date.today().year
    return{'year':year}
