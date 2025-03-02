from rest_framework import viewsets
from rest_framework.response import Response

from user.models import Author, Book
from user.serializers import (
    BooksWithAuthorNameSerializer,
    AuthorsWithBookNameSerializer,
    AuthorsWithoutBookSerializer,
    AuthorsWithSmallerBookPriceSerializer
)


class BooksWithAuthorNameViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Book.book_manager.books_with_author_name()
        serializer = BooksWithAuthorNameSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorsWithBooksNameViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_with_books()
        serializer = AuthorsWithBookNameSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorsWithSmallerBookPriceViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_with_smaller_book_price()
        serializer = AuthorsWithSmallerBookPriceSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorWithoutBookViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_without_books()
        serializer = AuthorsWithoutBookSerializer(queryset, many=True)
        return Response(serializer.data)
