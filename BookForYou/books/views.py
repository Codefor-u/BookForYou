from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CustomAuthenticationForm,RegistrationForm,BookForm
from .models import Book
 
def home(request):
    is_user_authenticated = request.user.is_authenticated
    return render(request, 'home.html', {'is_user_authenticated': is_user_authenticated})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def loginuser(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('display_portfolio')
    else:
        form = BookForm()
    return render(request, 'books/add_books.html', {'form': form})

def display_portfolio(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/display_portfolio.html', {'books': books})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('display_portfolio')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_books.html', {'form': form, 'book': book})
