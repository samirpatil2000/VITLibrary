from django.urls import path
from .views import books,bookDetailView,aboutUs,contactUs,index

urlpatterns = [
    # path('',BookListView.as_view(),name='book_list'),
    path('',index,name='index'),
    path('books/',books,name='book_list'),
    path('book/<str:slug>',bookDetailView,name='book_detail'),
    path('aboutus/',aboutUs,name='about_us'),
    path('contactus/',contactUs,name='contact_us')

 ]