# project_urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
     path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # Add other project-specific URL patterns as needed
]
