from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from .forms import RegistrationForm
from django.contrib import messages
from django.views import View
#Password for test user is tanvi@123
# Create your views here.
def home(request):
    # context = {
    #     'variable' : "This is sent"
    # }
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'home.html')
    
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'home.html', {'form': form})
    