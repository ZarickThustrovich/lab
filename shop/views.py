from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Lot, Session, SessionChatHistory


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
        active_sessions = Session.objects.filter(is_active=True).values()
        return JsonResponse({'active_sessions': list(active_sessions)}, safe=False)
        

def get_chat_history(request, session_uuid):
    if request.method == 'GET':
        chat_history = SessionChatHistory.objects.filter(session__session_uuid=session_uuid).values()
        return JsonResponse({'chat_history': list(chat_history)}, safe=False)