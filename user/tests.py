from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import Author, Book, BookAuthor


class APIViewsTests(APITestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')
        self.author3 = Author.objects.create(name='Author 3')
        self.author4 = Author.objects.create(name='Author 4')
        self.book1 = Book.objects.create(title='Book 1', price=123)
        self.book2 = Book.objects.create(title='Book 2', price=456)
        self.book3 = Book.objects.create(title='Book 3', price=789)
        self.book4 = Book.objects.create(title='Book 4', price=999)
        self.book_author1 = BookAuthor.objects.create(author=self.author1, book=self.book4)
        self.book_author2 = BookAuthor.objects.create(author=self.author1, book=self.book1)
        self.book_author3 = BookAuthor.objects.create(author=self.author2, book=self.book2)
        self.book_author3 = BookAuthor.objects.create(author=self.author3, book=self.book3)
        self.header = {"Authentication": settings.AUTHENTICATION_TOKEN}

    def test_authentication(self):
        url = reverse('authors-without-book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authors_without_books(self):
        url = reverse('authors-without-book-list')
        response = self.client.get(url, headers=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_authors_with_smaller_book_price(self):
        url = reverse('authors-with-smaller-book-price-list')
        response = self.client.get(url, headers=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_authors_with_books(self):
        url = reverse('authors-with-book-title-list')
        response = self.client.get(url, headers=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_books_with_authors(self):
        url = reverse('books-with-author-name-list')
        response = self.client.get(url, headers=self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
