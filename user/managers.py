from django.db.models import Manager, Prefetch, Min, F


class AuthorManager(Manager):
    def authors_without_books(self):
        from user.models import BookAuthor
        return self.exclude(id__in=BookAuthor.objects.values_list('author', flat=True))

    def authors_with_books(self):
        from user.models import BookAuthor
        return self.prefetch_related(
            Prefetch(
                'bookauthor_set',
                queryset=BookAuthor.objects.select_related('book'),
                to_attr='bookauthor_books'
            )
        )

    def authors_with_smaller_book_price(self):
        return self.annotate(min_price=Min('bookauthor__book__price'))


class BookManager(Manager):
    def books_with_author_name(self):
        from user.models import BookAuthor
        return self.prefetch_related(
            Prefetch(
                'bookauthor_set', queryset=BookAuthor.objects.select_related('author'))
            ).annotate(
                author_name=F('bookauthor__author__name')
            )
