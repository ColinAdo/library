from django.shortcuts import render, get_object_or_404
from .models import Book

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
