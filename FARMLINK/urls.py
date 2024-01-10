from django.urls import path

from FARMLINK.views import *

urlpatterns = [
    path('',login,name='login'),
]