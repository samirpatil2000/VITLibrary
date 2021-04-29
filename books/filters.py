import django_filters
from .models import Book,Category


class BookFilter(django_filters.Filter):
    class Meta:
        model=Book
        fields=[
            'category',
            'name',
            'year',
            'stream',
        ]