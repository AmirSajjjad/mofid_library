from django.db import models
from user.managers import AuthorManager, BookManager


class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    author_manager = AuthorManager()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    objects = models.Manager()
    book_manager = BookManager()

    def __str__(self):
        return self.title

    #TODO: class Meta


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.book}"
