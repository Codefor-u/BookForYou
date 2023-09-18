from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("about", views.about,name = "about"),
    path("contact", views.contact,name = "contact"),
    path('login',views.login,name = "login"),
    path('logout',views.logout,name = "logout"),
    
   
]
