from django.urls import path
from .views import books

urlpatterns = [
    # path('',BookListView.as_view(),name='book_list'),
    path('',books,name='book_list'),
    # path('<category>/<strem>/<year>',books,name='book_list'),

 ]