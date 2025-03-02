from rest_framework import serializers
from user.models import Author, Book


class BooksWithAuthorNameSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author_name']

    def get_author_name(self, obj):
        return obj.author_name


class AuthorsWithBookNameSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'books']

    def get_books(self, obj):
        return [book_author.book.title for book_author in obj.bookauthor_books]


class AuthorsWithSmallerBookPriceSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'min_price']

    def get_min_price(self, obj):
        return obj.min_price


class AuthorsWithoutBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
