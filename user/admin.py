from django.contrib import admin
from user.models import Author, Book, BookAuthor


@admin.register(Author, Book, BookAuthor)
class AuthorAdmin(admin.ModelAdmin):
    pass