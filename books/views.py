from django.shortcuts import render, redirect
from .models import Book,Category
from .filters import BookFilter
from .forms import BookFilterForm
from django_filters.views import FilterView
# Create your views here.

from account.models import Account

empty_string = ''

def is_valid_params(param):
    return param!=empty_string and param is not None

def index(request):
    context={
        'image':"https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_1':"https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_2':"https://images.unsplash.com/photo-1533327325824-76bc4e62d560?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80"
    }
    return render(request,'books/index.html',context)


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

    if is_valid_params(category):
        category_=Category.objects.get(id=category)
        queryset = queryset.filter(category=category)
        which_query+=str(category_.name)
        which_query += " , "

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


def aboutUs(request):
    return render(request,'books/about_us.html')

def contactUs(request):
    return render(request,'books/contactUS.html')



