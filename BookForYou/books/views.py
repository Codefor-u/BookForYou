from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'variable' : "This is sent"
    # }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')




 