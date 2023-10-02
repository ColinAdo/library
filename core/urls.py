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
]