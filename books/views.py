from django.shortcuts import render, redirect
from .models import Book,Category
from .filters import BookFilter
from .forms import BookFilterForm
from django_filters.views import FilterView
# Create your views here.


empty_string = ''

def is_valid_params(param):
    return param!=empty_string and param is not None


def bookDetailView(request,slug):
    context={
        'object':Book.objects.get(slug=slug)
    }
    return render(request,'books/book_detail.html',context)

def books(request):
    queryset = Book.objects.all()

    which_query=''
    form=BookFilterForm()

    category = request.GET.get('category')
    year = request.GET.get('year')
    stream = request.GET.get('stream')

    if is_valid_params(year):
        queryset = queryset.filter(year=year)
        which_query+=year
        which_query += " , "

    if is_valid_params(stream):
        queryset = queryset.filter(stream=stream)
        which_query += stream
        which_query += " , "
    context={
        'form':form,
        'books':queryset,
    }
    if is_valid_params(which_query):
        context['which_query']=which_query
    return  render(request,'books/book_list.html',context)




