from .models import Book,Category,Notes,ContactUs
from django import forms

class BookFilterForm(forms.ModelForm):

    class Meta:
        model=Book
        fields=[
            'category',
            # 'name',
            # 'year',
            # 'stream',
        ]


class UploadBooks(forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'category',
            'name',
            'description',
            'author',
            'thumbnail',
            'pdf_file',
            'google_drive_url',
            'is_syllabus',
            'year',
            'stream',
        ]

class UploadNotes(forms.ModelForm):
    class Meta:
        model=Notes
        fields=[
            'name',
            'description',
            'thumbnail',
            'pdf_file',
            'google_drive_url',
            'year',
            'stream',
            'term',
            'subject',
                ]

class NotesFilterForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=[
            # 'name',
            'year',
            'stream',
            'term',
            # 'subject',
        ]
class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=['full_name','email','query']