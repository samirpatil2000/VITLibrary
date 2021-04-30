from django.urls import path
from .views import books,bookDetailView

urlpatterns = [
    # path('',BookListView.as_view(),name='book_list'),
    path('',books,name='book_list'),
    path('book/<str:slug>',bookDetailView,name='book_detail'),

 ]