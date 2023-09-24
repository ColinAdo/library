from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def home(request):
    template = 'core/index.html'
    books = Book.objects.all().order_by('-date_posted')
    context = {
        'books': books
    }
    return render(request, template, context=context)

def books_details(request, book_id):
    template = 'core/books-details.html'
    b = get_object_or_404(Book, bid=book_id)
    context = {
        'b': b
    }
    return render(request, template, context)

def category_book(request, category_id):
    template = 'core/category-books.html'
    category = get_object_or_404(Category, cid=category_id)

    books = Book.objects.filter(category=category).order_by('-date_posted')
    context = {
        'books': books,
        'category': category
    }
    return render(request, template, context)
