from django.urls import resolve, reverse
from urllib.parse import quote
import pytest

from core.views import (
    home,
    books_details,
    search,
    read,
    favourite_add,
    favourite_list,
    likes_add,
    review_list,
)

@pytest.fixture
def book(request, book_factory):
    return book_factory(title="Test Book")

@pytest.mark.django_db
class TestUrls:
    def test_home_url(self):
        found = resolve('/')
        assert found.func == home
        assert reverse('home') == '/'

    def test_books_details_url(self, book):
        found = resolve(f"/books-details/{book.bid}")

        """
            Basically what's happening here is that, when trying to test this code without encoding it,
            it will most likely to fail because of difference in the URL encoding.
            In this case, the '?' was replaced with %3F which on this case need to be encoded to '?',
            This is where quoting comes in play.
        """
        expected_url = f"/books-details/{quote(book.bid)}"

        assert found.func == books_details
        assert reverse("book_details", args=[f"{book.bid}"]) == expected_url

    def test_search_url(self):
        found = resolve('/search/')

        assert found.func == search
        assert reverse('search') == '/search/'

    def test_read_book_url(self, book):
        found = resolve(f'/read/{book.bid}/')

        expected_url = f"/read/{quote(book.bid)}/"

        assert found.func == read
        assert reverse('read', args=[f"{book.bid}"]) == expected_url

    def test_add_favorites_url(self, book):
        found = resolve(f'/favourites/{book.bid}/')

        expected_url = f"/favourites/{quote(book.bid)}/"

        assert found.func == favourite_add
        assert reverse('favourite_add', args=[f"{book.bid}"]) == expected_url


    def test_favourite_list_url(self):
        found = resolve("/favourite/list/")

        assert found.func == favourite_list
        assert reverse('favourite_list') == "/favourite/list/"

    def test_add_likes_url(self, book):
        found = resolve(f"/like/{book.bid}/")

        expected_url = f"/like/{quote(book.bid)}/"
        assert found.func == likes_add
        assert reverse('likes_add', args=[f"{book.bid}"]) == expected_url

    def test_review_list_url(self, book):
        found = resolve(f"/review/list/{book.bid}/")

        expected_url = f"/review/list/{quote(book.bid)}/"
        assert found.func == review_list
        assert reverse('review_list', args=[f"{book.bid}"]) == expected_url
