from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Автор"
        verbose_name_plural="Авторы"


def image_directory(instance, filename):
    return 'book_{0}/{1}'.format(instance.id, filename)


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name="Жанр"
        verbose_name_plural="Жанры"


class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pic_link = models.ImageField(upload_to=image_directory)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '. ' + self.author.name 

    class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книга"


class Lot(models.Model):
    start_price = models.CharField(max_length=100)
    end_price = models.CharField(max_length=100)
    current_price = models.CharField(max_length=100)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField()
    expiration_date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    expired = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name="Лот"
        verbose_name_plural="Лот"
        
       
class Comment(models.Model):
    textarea = models.TextField()
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.textarea

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural="Комментарии"


class Counter(models.Model):
    value = models.CharField(max_length=255, null=False, blank=False)
    