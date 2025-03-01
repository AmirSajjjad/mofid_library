from django.db.models import Manager, Prefetch, Min, F

from user.models import BookAuthor


class AuthorManager(Manager):
    def authors_without_books(self):
        return self.exclude(id__in=BookAuthor.objects.values_list('author', flat=True))

    def authors_with_books(self):
        authors = self.prefetch_related(
            Prefetch(
                'bookauthor_set',
                queryset=BookAuthor.objects.select_related('book'),
                to_attr='bookauthor_books'
            )
        )
        return authors

    def authors_with_smaller_book_price(self):
        return self.annotate(min_price=Min('bookauthor__book__price'))


class BookManager(Manager):
    def books_with_author(self):
        return self.prefetch_related(
            Prefetch('bookauthor_set', queryset=BookAuthor.objects.select_related('author'))
        ).annotate(
            author_names=F('bookauthor__author__name')
        )
