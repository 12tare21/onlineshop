from django.urls import path
from . import views

urlpatterns = [
    path(r'<slug:slug>-<int:product_id>',views.detail,name="detail"),
    path(r'categories/<slug:slug>',views.category,name="category"),
    path(r'create',views.create,name='create'),
    path(r'search',views.search,name='search'),
    path(r'<slug:slug>-<int:product_id>/update',views.update,name='update'),
    path(r'<slug:slug>-<int:product_id>/delete',views.delete,name='delete'),
]
