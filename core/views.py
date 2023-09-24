from django.shortcuts import render
from .models import Book

def home(request):
    template = 'core/index.html'
    books = Book.objects.all().order_by('-date_posted')
    context = {
        'books': books
    }
    return render(request, template, context=context)
