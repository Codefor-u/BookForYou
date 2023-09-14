from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'variable' : "This is sent"
    # }
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is Aboutpage")

def services(request):
    return HttpResponse("This is Servicespage")




 