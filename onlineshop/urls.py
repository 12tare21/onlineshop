from django.contrib import admin
from django.urls import path,include
from products import views as productviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',productviews.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
