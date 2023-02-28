from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.members, name='members'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('ci/', views.compound_interest, name='compound_interest'),
    path('si/', views.simple_int, name='simple'),
    path('login/', auth_view.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    

]         