from django.urls import path, include

from . views import logout_view
from . views import edit_post, delete_post
from . import views

urlpatterns = [
    path('official-profile/',views.Government,name="official-profile"),
    path('government-profile',views.Government,name="government-profile"),
    path('post',views.post,name="post"),
    path('policies/',views.policies,name="policies"),
    path('logout/',logout_view,name='logout'),
    path('edit_post/<int:post_id>/', edit_post.as_view(), name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]