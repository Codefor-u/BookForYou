# book/views.py
from django.shortcuts import render, redirect
from .forms import BookUploadForm
from .models import Book
from django.contrib.auth.decorators import login_required

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('home')
    else:
        form = BookUploadForm()
    return render(request, 'book/upload_book.html', {'form': form})

def user_books(request, username):
    books = Book.objects.filter(user__username=username)
    return render(request, 'book/user_books.html', {'books': books, 'username': username})
