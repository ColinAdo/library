from pytest_factoryboy import register

from .factory import CategoryFactory, BookFactory, ProgressFactory, ReviewFactory

register(CategoryFactory)
register(BookFactory)
register(ProgressFactory)
register(ReviewFactory)