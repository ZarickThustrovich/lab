from django.shortcuts import render
from .models import Book


def books_catalog(request):
    if request.method == "GET":
        books = Book.objects.filter(is_active=True)
        return render(request, 'catalog.html', {'books': books})