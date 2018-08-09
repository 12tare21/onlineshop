from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('settings',views.settings,name='settings'),
    path('profile',views.yourprofile,name='profilepage'),
    path('change-password',views.password_change,name='password'),
    path('delete',views.delete,name='delete'),
    path('<slug:user_slug>',views.userpage,name='userpage'),
]
