from django.urls import path
from . import views

urlpatterns = [
    path(r'<slug:slug>-<int:product_id>',views.detail,name="detail"),
    path(r'categories/<slug:slug>',views.category,name="category"),
    path(r'create',views.create,name='create'),
]
