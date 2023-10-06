from django.urls import path
from .import views

urlpatterns = [
    # Home url
    path("", views.home, name="home"),

    # Books urls
    path("books-details/<str:book_id>", views.books_details, name="book_details"),
    path("category-books/<str:category_id>", views.category_book, name="category_books"),

    # Search url
    path('search/', views.search, name="search"),

    # Reading the pdf
    path('read-pdf/<str:book_id>/', views.read_pdf, name="read"),
    path('read-new-pdf/<str:book_id>/', views.create_and_read, name="create_and_read"),

    # Favourites
    path('add-remove-favourites/<str:book_id>/', views.favourite_add, name="favourite_add"),
    path('favourite-book-list/', views.favourite_list, name="favourite_list"),

    # Likes
    path('add-remove-like/<str:book_id>/', views.likes_add, name='likes_add'),

    # Review 
    path('review-list/<str:book_id>/', views.review_list, name='review_list'),
]