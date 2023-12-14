import pytest

from datetime import timedelta

from django.utils import timezone

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_return(self, category_factory):
        category = category_factory(title="Test Category")

        assert category.__str__() == "Test Category"

class TestBookModel:
    def test_str_return(self, book_factory):
        book = book_factory(title="Test Book")

        assert book.__str__() == "Test Book"

    def test_is_new(self, book_factory):
        resent_book = book_factory(title="New Book", date_posted=timezone.now())

        future_book = book_factory(title="Future Book", date_posted=timezone.now() + timedelta(days=7))

        threshold_days = 7
        with_in_threshold = book_factory(title="Threshold Days", date_posted=timezone.now() + timedelta(days=threshold_days - 1))

        outside_threshold = book_factory(title="Outside Threshold", date_posted=timezone.now() + timedelta(days=threshold_days + 1))

        assert resent_book.is_new() is True
        assert future_book.is_new() is True
        assert with_in_threshold.is_new() is True
        assert outside_threshold.is_new() is True


class TestProgressModel:
    def test_str_return(self, progress_factory, book_factory):
        book = book_factory(title="Test Progress")
        progress = progress_factory(book=book)

        assert progress.__str__() == "Test Progress"

    def test_set_finish_date(self, progress_factory, book_factory):
        book = book_factory(title="Test Progress")
        progress = progress_factory(book=book)

        assert progress.finish_date is None

        progress.set_finish_date()

        assert progress.finish_date is not None
        assert progress.finish_date == progress.start_date + timedelta(minutes=2)

    def test_days_remaining(self, progress_factory, book_factory):
        book = book_factory(title="Test Progress")
        progress = progress_factory(book=book)

        assert progress.days_remaining is None

        progress.set_finish_date()

        assert progress.days_remaining is not None

    def test_mark_as_complete(self, progress_factory, book_factory):
        book = book_factory(title="Test Progress")
        progress = progress_factory(book=book)

        progress.mark_as_complete()

        assert progress.is_complete == True
        assert progress.finish_date is not None


class TestReviewModel:
    def test_str_return(self, review_factory):
        review = review_factory(comment="Test Review")

        assert review.__str__() == "Test Revie"
