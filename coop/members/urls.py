from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]