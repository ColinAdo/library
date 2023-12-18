from core.admin import BookAdmin

import pytest 

@pytest.fixture
def book(request, book_factory):
    return book_factory(
        title="Test category",
        cover_image="/media/profile/cover/cover.jpg",
        description= "This test will now pass only if the short"
        )
    
@pytest.mark.django_db
class TestBookAdmin:
    def test_display_cover_image(self, book):
        book_admin = BookAdmin(book, admin_site=True) # admin_site=True
        assert book_admin.display_cover_image(book) == '<img src="{}" style="border-radius: 5px; width="50" height="50" />'.format(book.cover_image.url)

    def test_short_description(self, book):
        book_admin = BookAdmin(book, admin_site=True)  # admin_site=True
        assert book_admin.short_description(book)

    def test_long_description(self, book):
        book.description = "This test will now pass only if the short_description function raises an AssertionError, indicating that the description is longer than 10 words. Adjust the expected failure condition based on your actual expectations."

        book_admin = BookAdmin(book, admin_site=True)
        assert book_admin.short_description(book) != book.description 
        
