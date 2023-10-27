from django.contrib import admin
from .models import Author, Genre, Book, Lot, Comment


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Lot)
admin.site.register(Comment)