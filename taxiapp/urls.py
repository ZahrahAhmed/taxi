from django.urls import path
from . import views

app_name = 'taxiapp'

urlpatterns = [
	path('home/', views.home, name="home"),
	path('signup/', views.usersignup, name='signup'),
	path('login/', views.userlogin, name='login'),
	path('logout/', views.userlogout, name='logout'),
	path('restaurant/home/', views.restaurant_home, name="restaurant_home"),
	path('restaurant/signup/', views.restaurant_signup, name="restaurant_signup"),
	path('restaurant/signin/', views.restaurant_signin, name="restaurant_signin"),
	path('restaurant/signout/', views.restaurant_signout, name="restaurant_signout"),
]
