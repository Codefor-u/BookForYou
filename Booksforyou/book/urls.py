# book/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_book, name='upload_book'),
    path('<str:username>/books/', views.user_books, name='user_books'),
]
