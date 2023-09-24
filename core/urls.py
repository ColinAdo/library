from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books-details/<str:book_id>", views.books_details, name="book_details"),
]