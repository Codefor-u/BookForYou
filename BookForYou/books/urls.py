from django.contrib import admin
from django.urls import path
from books import views
from books.forms import PasswordResetForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name = "Home"),
    path("about", views.about,name = "about"),
    path("contact", views.contact,name = "contact"),
    path('login',views.loginuser,name = "loginuser"),
    path('logout',views.logoutuser,name = "logoutuser"),
    path('register', views.RegistrationView.as_view(), name="register"),
#   path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', form_class=PasswordResetForm, success_url='/accounts/password-reset/done/'), name="password-reset"), # Passing Success URL to Override default URL, also created password_reset_email.html due to error from our app_name in URL
#   path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
#   path('accounts/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', form_class=SetPasswordForm, success_url='/accounts/password-reset-complete/'), name="password_reset_confirm"), # Passing Success URL to Override default URL
#   path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),
 ]
