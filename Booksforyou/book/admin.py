# book/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'user')  # Add 'user' to the list display

admin.site.register(Book, BookAdmin)
