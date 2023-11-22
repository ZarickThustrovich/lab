from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Lot, Session


def get_books_catalog(request):
    if request.method == 'GET':
        books = Book.objects.filter(is_active=True).values()
        return JsonResponse({'books': list(books)}, safe=False)


def get_specific_book(request, id):
    if request.method == 'GET':
        book = Book.objects.get(id=id)
        return JsonResponse({'book': book}, safe=False)
        
        
def get_specific_lot(request, id):
    if request.method == 'GET':
        lot = Lot.objects.get(id=id)
        return JsonResponse({'lot': lot}, safe=False)
        
        
def get_active_sessions(request):
    if request.method == 'GET':
        active_sessions = Session.objects.filter(is_active=True)
        return JsonResponse({'active_sessions': list(active_sessions)}, safe=False)