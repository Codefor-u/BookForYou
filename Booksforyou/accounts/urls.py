# accounts/urls.py
from django.urls import path
from . import views
from book.views import upload_book

urlpatterns = [
    path('', views.index_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile_view, name='profile'),
    path('search/', views.user_search, name='search'),
     path('edit-profile/', views.profile_edit, name='profile_edit'),
     path('profile/<str:username>/', views.user_profile, name='profile'),
     path('add_books/', upload_book, name='add_books'),
    # path('password_reset/', views.password_reset_view, name='password_reset'),
]
