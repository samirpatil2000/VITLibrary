from django.urls import path
from .views import (books,bookDetailView,aboutUs,
                    contactUs,index,getBookDownloadUrl,
                    uploadBook,stream_wise_books,category_wise_books,
                    notes,notesDetailView,uploadNotes,upload_book_request,
                    accept_book_request,accept_notes_request,
                    remove_book,remove_notes,
                    )

urlpatterns = [
    # path('',BookListView.as_view(),name='book_list'),
    path('',index,name='index'),

    # listView
    path('books/',books,name='book_list'),
    path('notes/',notes,name='notes_list'),
    path('books/stream/<str:stream>',stream_wise_books,name='book_list_stream'),
    path('books/cat/<str:category>',category_wise_books,name='category_wise_books'),

    path('book/<str:slug>',bookDetailView,name='book_detail'),
    path('notes/<str:slug>',notesDetailView,name='notes_detail'),

    path('book-download/<str:slug>',getBookDownloadUrl,name='download_book'),

    path('uploadBook/',uploadBook,name='upload_book'),
    path('uploadNotes/',uploadNotes,name='upload_notes'),

    path('upload-book-requests/',upload_book_request,name='upload_book_requests'),

    path('accept-book-requests/<request_book_slug>',accept_book_request,name='accept_book_request'),
    path('accept-notes-requests/<request_notes_slug>',accept_notes_request,name='accept_notes_request'),

    path('remove_book/<request_book_slug>', remove_book, name='remove_book'),
    path('remove_notes/<request_notes_slug>', remove_notes, name='remove_notes'),

    path('aboutus/',aboutUs,name='about_us'),
    path('contactus/',contactUs,name='contact_us'),


 ]


"""
--- 1. profile page ( add books uploaded by that user ) first name and last name
--- 2. upload request page
3. upload request page-ui
--- . google drive link

--- 2. create class cr table and associate all user within is class 
--- 2. add books form
--- 3. download url
--- 4. search button


6 . security packages -
                      - honeypot 
                      - defender
                      - django defender

"""