"""Project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.gmail_view),
    path('signin/', views.signin_view),
    path('signup/', views.signup_view),
    path('home/', views.login_members),
    path('signup/',views.data_from_signup),
    path('logina/',views.data_from_view),
    path('delete/',views.delete_members),
    path('update/',views.update_members),
    path('updatenew/',views.update_new),
    
    
    
    
    
]
