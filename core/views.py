from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Category, Review, Progress
from .forms import ReviewForm
from userAuths.models import CustomUser

@login_required(login_url='sign_in')
def home(request):
    template = 'core/index.html'
    books = Book.objects.annotate(review_count=Count('review')).order_by('-date_posted')
    context = {
        'books': books
    }
    return render(request, template, context=context)

@login_required(login_url='sign_in')
def books_details(request, book_id):
    template = 'core/books-details.html'
    login_user = request.user
    user = CustomUser.objects.get(username=login_user)

    b = get_object_or_404(Book, bid=book_id)
    reviews = Review.objects.filter(book=b).order_by('-date')

    try:
        progress = Progress.objects.get(user=user, book=b, is_complete=False)
    except Progress.DoesNotExist:
        progress = None
    
    # Query to check if the user has any ongoing progress
    ongoing_progress = Progress.objects.filter(user=user, is_complete=False).exists()

   
    favourite_exists = b.favourites.filter(id=login_user.id).exists()
    likes_exists = b.likes.filter(id=login_user.id).exists()
    user_exists = b.readers.filter(id=user.id).exists()

    context = {
        'b': b,
        'reviews': reviews,
        'progress': progress,
        'ongoing_progress': ongoing_progress,
        'favourite_exists': favourite_exists,
        'likes_exists': likes_exists,
        'user_exists': user_exists
    }
    return render(request, template, context)

@login_required(login_url='sign_in')
def category_book(request, category_id):
    template = 'core/category-books.html'
    category = get_object_or_404(Category, cid=category_id)

    books = Book.objects.filter(category=category).order_by('-date_posted')
    context = {
        'books': books,
        'category': category
    }
    return render(request, template, context)

@login_required(login_url='sign_in')
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

@login_required(login_url='sign_in')
def read(request, book_id):
    template = 'core/read.html'
    user = request.user
    book = get_object_or_404(Book, bid=book_id)

    if not book.readers.filter(id=user.id).exists():
        book.readers.add(user.id)
        created = Progress.objects.create(user=user, book=book, is_reading=True)
        if created:
            created.set_finish_date()
    
    progress = Progress.objects.get(user=user, book=book, is_reading=True)    
    pdf_url = book.pdf_file.url
    context = {
        'pdf_url': pdf_url,
        'progress': progress
    }

    return render(request, template, context)

@login_required(login_url='sign_in')
def favourite_add(request, book_id):
    user_id = request.user.id
    book = get_object_or_404(Book, bid=book_id)
    if book.favourites.filter(id=user_id).exists():
        book.favourites.remove(user_id)
    else:
        book.favourites.add(user_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='sign_in')
def favourite_list(request):
    template = 'core/favourites.html'
    login_user = request.user
    p = get_object_or_404(CustomUser, username=login_user.username)
    books = Book.objects.filter(favourites=login_user).order_by('-date_posted')

    book = None
    for book in books:
        likes_exists = book.likes.filter(id=login_user.id).exists()
    context = {
        'p': p,
        'books': books,
        'likes_exists': likes_exists
    }
    return render(request, template, context)

@login_required(login_url='sign_in')
def likes_add(request, book_id):
    login_user = request.user.id
    book = get_object_or_404(Book, bid=book_id)

    if book.likes.filter(id=login_user).exists():
        book.likes.remove(login_user)
    else:
        book.likes.add(login_user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='sign_in')
def review_list(request, book_id):
    template = 'core/books-reviews.html'
    login_user = request.user
    user = CustomUser.objects.get(username=login_user)

    b = get_object_or_404(Book, bid=book_id)
    reviews = Review.objects.filter(book=b).order_by('-date')
    user_review = Review.objects.filter(user=user, book=b).first()

    try:
        progress = Progress.objects.filter(user=user)
    except Progress.DoesNotExist:
        progress = None
   
    if request.method == 'POST':
        form =  ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = b
            review.save()
            messages.success(request, 'Review added successfully')
            return redirect('review_list', book_id)
    else:
        form = ReviewForm()

    favourite_exists = b.favourites.filter(id=login_user.id).exists()
    likes_exists = b.likes.filter(id=login_user.id).exists()

    context = {
        'b': b,
        'reviews': reviews,
        'user_review': user_review,
        'form': form,
        'progress': progress,
        'favourite_exists': favourite_exists,
        'likes_exists': likes_exists,
    }
    return render(request, template, context)
