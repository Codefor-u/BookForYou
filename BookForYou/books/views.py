from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
#Password for test user is tanvi@123
# Create your views here.
def index(request):
    # context = {
    #     'variable' : "This is sent"
    # }
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            return redirect("/")
        else:
            return render(request,'login.html')
    
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')





 