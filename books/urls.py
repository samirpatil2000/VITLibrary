from django.urls import path
from .views import (books,bookDetailView,aboutUs,
                    contactUs,index,getBookDownloadUrl,
                    uploadBook,stream_wise_books,category_wise_books,
                    notes,notesDetailView
                    )

urlpatterns = [
    # path('',BookListView.as_view(),name='book_list'),
    path('',index,name='index'),
    path('books/',books,name='book_list'),
    path('books/stream/<str:stream>',stream_wise_books,name='book_list_stream'),
    path('books/cat/<str:category>',category_wise_books,name='category_wise_books'),
    path('book/<str:slug>',bookDetailView,name='book_detail'),
    path('notes/<str:slug>',notesDetailView,name='notes_detail'),
    path('book-download/<str:slug>',getBookDownloadUrl,name='download_book'),
    path('uploadBook/',uploadBook,name='upload_book'),
    path('aboutus/',aboutUs,name='about_us'),
    path('contactus/',contactUs,name='contact_us'),
    path('notes/',notes,name='notes_list'),

 ]


"""
1. profile page ( add books uploaded by that user )
2. create class cr table and associate all user within is class 
--- 2. add books form
--- 3. download url
--- 4. search button


"""