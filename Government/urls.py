from django.urls import path, include

from . import views

urlpatterns = [
    path('official-profile/',views.Government,name="official-profile"),
    # path('',views.Government,name="government-home"),
]