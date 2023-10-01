from django.contrib import admin
from django.urls import path
from books import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.loginuser, name="loginuser"),  # Updated login URL
    path("logout", views.logoutuser, name="logoutuser"),  # Updated logout URL
    path("signup", views.signup, name="signup"),  # Updated registration URL
]
