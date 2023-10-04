from django.contrib import admin
from django.urls import path
from books import views
from django.contrib.auth import views as auth_views

# app_name = "books"
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.loginuser, name="loginuser"),  # Updated login URL
    path("logout", views.logoutuser, name="logoutuser"),  # Updated logout URL
    path("signup", views.signup, name="signup"),  # Updated registration URL
    path('add_book', views.add_book, name='add_book'),
    path('portfolio', views.display_portfolio, name='display_portfolio'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('profile_search', views.profile_search, name='profile_search'),

]
