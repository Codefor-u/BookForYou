# Create a view for the project's homepage

from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
