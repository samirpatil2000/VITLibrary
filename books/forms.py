from .models import Book,Category
from django import forms

class BookFilterForm(forms.ModelForm):

    class Meta:
        model=Book
        fields=[
            'category',
            # 'name',
            'year',
            'stream',
        ]