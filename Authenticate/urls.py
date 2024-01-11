from django.urls import path

from Authenticate.views import *

urlpatterns = [
    path('',login,name='login'),
]