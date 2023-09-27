from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book, Category, Review
from userAuths.models import CustomUser

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

def search(request):
    template = 'core/search.html'
    query = request.GET.get('q')

    users = CustomUser.objects.filter(username__icontains=query)
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)).order_by('-date_posted')
    categories = Category.objects.filter(title__icontains=query).order_by('-date')
    reviews = Review.objects.filter(comment__icontains=query).order_by('-date')

    conetxt = {
        'users': users,
        'books': books,
        'categories': categories,
        'reviews': reviews,
        'query': query,
    }
    return render(request, template, conetxt)
