from multiprocessing import context
from tkinter import E
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from books.models import Book
from category.models import BookCategory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
@login_required

def books(request,category_slug=None):
    categories = None
    books = None
    if category_slug != None:
        categories = get_object_or_404(BookCategory, slug=category_slug)
        books = Book.objects.filter(category=categories)
        paginator = Paginator(books, 9)
        page = request.GET.get('page')
        paged_books = paginator.get_page(page)
        books_count = books.count()
         
    else:
         books = Book.objects.all().order_by('id')
         paginator = Paginator(books, 9)
         page = request.GET.get('page')
         paged_books = paginator.get_page(page)
         books_count = books.count()
    context ={
        'books': paged_books,
        'books_count':books_count,
    }
    return render(request,'books.html', context)


def read_books(request, category_slug, book_slug ):
    try:
        single_book = Book.objects.get(category__slug=category_slug, slug= book_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_book': single_book,
        
    }
    return render(request, 'read_books.html',context)