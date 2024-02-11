from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.homepage,name='others-profile'),
    # path('',views.User,name='user-home'),
    path('weatherr/',views.weatherr,name='weatherr'),
    path('jobb/',views.jobb,name='jobb'),
    path('markett/',views.markett,name='markett'),
    path('policies',views.policies,name='policies'),
    path('profilee/',views.profilee,name='profilee'),
    path('logout/',views.user_logout,name='logout'),
    path('user-profilee/uploadd',views.uploadd,name='uploadd'),
    path('like-postt/<str:id>', views.likess, name='like-postt'),
    path('#/<str:id>', views.home_postt, name='home_postt'),
    path('profile/<str:username>/', views.profile_details, name='profile_details'),
    path('deletee/<str:id>', views.deletee, name='deletee-post'),
    path('search-resultss/', views.search_resultss, name='search_resultss'),
    path('followw/', views.followw, name='followw'),
   
]