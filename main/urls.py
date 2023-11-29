from django.urls import path
from .views import create_tweet, loginPage, logoutPage, signupPage, delete_tweet, user_profile, edit_profile, profile_view

urlpatterns = [
    path('', create_tweet, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signupPage, name='signup'),
    path('deletepost/<int:pk>', delete_tweet, name='deletepost'),
    path('profile/', user_profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
]