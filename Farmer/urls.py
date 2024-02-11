from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home,name="farmer-profile"),
    # path('',views.Farmer,name="farmer-home"),
    path('weather/',views.weather,name='weather'),
    path('job/',views.job,name='job'),
    path('market/',views.market,name='market'),
    path('policies',views.policies,name='policies'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_farmer,name='logout_farmer'),
    path('farmer-profile/upload',views.upload,name='upload'),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#/<str:id>', views.home_post, name='home_post'),
    path('profile/<str:username>/', views.user_profile, name='user-profile'),
    path('Farmerdelete/<str:id>/', views.delete_post, name='delete-post'),
    path('search-results/', views.search_results, name='search_results'),
    path('follow/', views.follow, name='follow'),
   
]