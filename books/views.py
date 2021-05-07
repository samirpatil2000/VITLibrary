from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book,Category,Notes,ContactUs
from .forms import BookFilterForm,UploadBooks,NotesFilterForm,ContactUsForm,UploadNotes
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.core.mail import send_mail, send_mass_mail, EmailMessage

from account.models import Account

empty_string = ''

def is_valid_params(param):
    return param!=empty_string and param is not None
STREAM=[
    'EXTC',
    'INFT',
    'CS',
    'ETRX',
    'BIOMED',
]
def index(request):
    stream_book_count=[]
    stream_notes_count=[]
    for stream in STREAM:
        stream_book_count.append(Book.objects.filter(stream__exact=stream).count())
        stream_notes_count.append(Notes.objects.filter(stream__exact=stream).count())


    category_book_count=[]
    categories=Category.objects.all()
    for category in categories:
        category_book_count.append(Book.objects.filter(category=category).count())
    context={
        'streams':zip(STREAM,stream_book_count,stream_notes_count),
        'categories':zip(categories,category_book_count),
        'image':"https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_1':"https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_2':"https://images.unsplash.com/photo-1533327325824-76bc4e62d560?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80"
    }

    return render(request,'books/index.html',context)


def bookDetailView(request,slug):
    book=Book.objects.get(slug=slug)
    context={
        'object':book
    }
    context['books_cat']=context['object'].category.all()
    context['books_count'] = len(context['books_cat'])
    print(context['books_count'])
    try:
        book_user=book.uploaded_by
        if request.user.is_authenticated:
            account = Account.objects.get(email=request.user.email)
            # if account.is_classcr and account.branch==book_user.branch and account.year==book_user.year:
            if (account.is_classcr and account.branch==book_user.branch and account.year==book_user.year) \
                    or request.user.is_superuser or request.user.is_staff:
            # context['delet']
                context['is_cr']=True
            # print(account)
    except:
        pass

    return render(request,'books/book_detail.html',context)


@login_required
def getBookDownloadUrl(request,slug):
    object=Book.objects.get(slug=slug)
    object.downloads.add(request.user)
    object.save()
    return redirect('book_detail',slug)


def books(request):
    # email = EmailMessage('Subject', 'Body', to=['samir.patil@vit.edu.in'])
    # email.send()
    queryset = Book.objects.all().filter(is_check=True)

    search_book=request.GET.get('search_book')


    which_query=''
    form=BookFilterForm()

    category = request.GET.get('category')
    year = request.GET.get('year')
    stream = request.GET.get('stream')

    if is_valid_params(search_book):
        queryset=queryset.filter(Q(name__icontains=search_book)|
                                 Q(author__icontains=search_book)|
                                 Q(category__name__icontains=search_book)|
                                 Q(stream__icontains=search_book)).distinct()
        which_query+=search_book


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
        'which_fun':"main",
        'form':form,
        'books':queryset,
        'count':queryset.count()
    }
    if is_valid_params(which_query):
        context['which_query']=which_query


    return  render(request,'books/book_list.html',context)

def notesDetailView(request,slug):

    context={
        'object':Notes.objects.get(slug=slug),
    }
    return render(request,'books/notes_detail.html',context)

def notes(request):
    queryset = Notes.objects.all().filter(is_check=True)

    # search_book = request.GET.get('search_book')

    which_query = ''
    form = NotesFilterForm()

    category = request.GET.get('category')
    year = request.GET.get('year')
    stream = request.GET.get('stream')
    term = request.GET.get('term')

    # if is_valid_params(search_book):
    #     queryset = queryset.filter(Q(name__icontains=search_book) |
    #                                Q(author__icontains=search_book) |
    #                                Q(category__name__icontains=search_book) |
    #                                Q(stream__icontains=search_book)).distinct()
    #     which_query += search_book


    if is_valid_params(year):
        queryset = queryset.filter(year=year)
        which_query += year
        which_query += " , "

    if is_valid_params(stream):
        queryset = queryset.filter(stream=stream)
        which_query += stream
        which_query += " , "


    if is_valid_params(term):
        queryset = queryset.filter(term=term)
        which_query += term
        which_query += " , "

    context = {
        'which_fun': "main",
        'form': form,
        'books': queryset,
        'count': queryset.count()
    }

    if is_valid_params(which_query):
        context['which_query'] = which_query
    return render(request,'books/notes_list.html',context)


def createSlug(title):
    slug_=""
    for i in title:
        if i!=" ":
            if ord(i)>=97:
                slug_+=i
            else:
                slug_+=chr(ord(i)+32)
        else:
            slug_+="-"
    return slug_

@login_required
def uploadBook(request):
    form=UploadBooks()
    if request.method=="POST":
        form=UploadBooks(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=request.POST.get('name')
            book=form.save(commit=False)
            book.uploaded_by=request.user
            book.is_check=False
            book.slug=createSlug(name)
            book.save()
            return redirect('book_detail',book.slug)
    context={
        'form':form
    }
    return render(request,'books/upload_book.html',context)

@login_required
def uploadNotes(request):
    form=UploadNotes()
    if request.method=="POST":
        form=UploadNotes(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=request.POST.get('name')
            notes=form.save(commit=False)
            notes.uploaded_by=request.user
            notes.slug=createSlug(name)
            notes.is_check=False
            notes.save()
            return redirect('notes_detail',notes.slug)
    context={
        'form':form
    }
    return render(request,'books/upload_notes.html',context)


def aboutUs(request):

    context={
        'image':"https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_1':"https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
        'image_2':"https://images.unsplash.com/photo-1533327325824-76bc4e62d560?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80"
    }
    return render(request,'books/about_us.html',context)

def contactUs(request):
    user=None
    if request.user.is_authenticated:
        user=request.user

    if request.method=="POST":
        full_name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        ContactUs.objects.create(full_name=full_name,email=email,query=desc)
        messages.success(request,"Your Messages Send Successfully ..!")
        return redirect('index')

    # form=ContactUsForm()
    # if request.method=="POST":
    #     form=ContactUsForm(request.POST or None)
    #     if form.is_valid():
    #         contact=form.save(commit=False)
    #         contact.save()
    #         messages.success(request,"Your Messages Send Successfully")
    context={
        # 'form':form,
        'initial_user':user
    }
    return render(request,'books/contactUS.html',context)

def stream_wise_books(request,stream):
    context={
        'which_fun':None,
        'books':Book.objects.filter(stream__exact=stream,is_check=True),
        'filter_by':stream,
    }
    return render(request,'books/book_list.html',context)


def category_wise_books(request,category):
    context={
        'which_fun':None,
        'books':Book.objects.filter(category__name=category,is_check=True),
        'filter_by':category,
    }
    return render(request,'books/book_list.html',context)

@login_required
def upload_book_request(request):
    # Account.objects.create(email="kanishka.gupta@vit.edu.in",password="123",branch="EXTC",is_classcr=True,year="S.E")
    account=Account.objects.get(email=request.user.email)
    if account.is_classcr or account.is_superuser or account.is_staff:
        context={
            # 'books':Book.objects.all().filter(is_check=False,year=account.year,stream=account.branch)
            'books':Book.objects.all().filter(is_check=False)
        }
        return render(request,'books/upload_book_request.html',context)
    else:
        messages.warning(request, "You don't have permissions to access this page")
        return redirect('index')


@login_required
def accept_book_request(request,request_book_slug):
    book=Book.objects.get(slug=request_book_slug)
    if request.user.is_classcr or request.user.is_superuser or request.user.is_staff:
        book.is_check=True
        book.save()
        return redirect('book_detail',request_book_slug)
    else:
        messages.warning(request, "You don't have permissions to access this page")
        return redirect('index')

