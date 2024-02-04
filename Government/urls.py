from django.urls import path, include

from . views import logout_view
from . import views

urlpatterns = [
    path('official-profile/',views.Government,name="official-profile"),
    path('government-profile',views.Government,name="government-profile"),
    path('post',views.post,name="post"),
    path('policies/',views.policies,name="policies"),
    path('logout/',logout_view,name='logout')
]