from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import (
    AuthorsWithBooksNameViewSet,
    AuthorWithoutBookViewSet,
    AuthorsWithSmallerBookPriceViewSet,
    BooksWithAuthorNameViewSet
)

router = DefaultRouter()
router.register(r'authors-with-book-title', AuthorsWithBooksNameViewSet, basename='authors-with-book-title')
router.register(r'authors-with-smaller-book-price', AuthorsWithSmallerBookPriceViewSet, basename='authors-with-smaller-book-price')
router.register(r'authors-without-book', AuthorWithoutBookViewSet, basename='authors-without-book')
router.register(r'books-with-author-name', BooksWithAuthorNameViewSet, basename='books-with-author-name')

# TODO: change routes:  user/...
urlpatterns = [
    path('', include(router.urls)),
]
