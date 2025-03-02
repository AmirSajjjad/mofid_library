from rest_framework import viewsets
from rest_framework.response import Response
from django.conf import settings

from user.models import Author, Book
from user.serializers import (
    BooksWithAuthorNameSerializer,
    AuthorsWithBookNameSerializer,
    AuthorsWithoutBookSerializer,
    AuthorsWithSmallerBookPriceSerializer
)

class CheckToken(viewsets.ViewSet):
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        auth_header = request.headers.get('Authentication')
        if auth_header != settings.AUTHENTICATION_TOKEN:
            self.permission_denied(request, message='Invalid authentication header')


class BooksWithAuthorNameViewSet(CheckToken, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Book.book_manager.books_with_author_name()
        serializer = BooksWithAuthorNameSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorsWithBooksNameViewSet(CheckToken, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_with_books()
        serializer = AuthorsWithBookNameSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorsWithSmallerBookPriceViewSet(CheckToken, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_with_smaller_book_price()
        serializer = AuthorsWithSmallerBookPriceSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorWithoutBookViewSet(CheckToken, viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Author.author_manager.authors_without_books()
        serializer = AuthorsWithoutBookSerializer(queryset, many=True)
        return Response(serializer.data)
