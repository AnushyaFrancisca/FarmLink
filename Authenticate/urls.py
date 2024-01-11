from django.urls import path

from Authenticate.views import *

urlpatterns = [
    path('',userlogin,name='login'),
    path('Admin/admin-dashboard',admin_dashboard,name='admin-dashboard')
]