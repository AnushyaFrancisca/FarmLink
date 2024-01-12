from django.urls import path

from Authenticate.views import *

urlpatterns = [
    path('login',userlogin,name='login'),
    path('Authenticate/register',register,name='register'),
    path('Admin/admin-dashboard',admin_dashboard,name='admin-dashboard'),
    path('Admin/about',about,name='about'),
    path('',base,name='base'),
]