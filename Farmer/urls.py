from django.urls import path, include

from . import views

urlpatterns = [
    path('farmer-profile/',views.Farmer,name="farmer-profile"),
    # path('',views.Farmer,name="farmer-home"),
]