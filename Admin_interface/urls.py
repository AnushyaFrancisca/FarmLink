from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Admin_interface),
]