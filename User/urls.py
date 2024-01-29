from django.urls import path, include

from . import views

urlpatterns = [
    path('others-profile/',views.User,name='others-profile'),
    # path('',views.User,name='user-home'),
]