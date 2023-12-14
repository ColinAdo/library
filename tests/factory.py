import factory

from django.contrib.auth import get_user_model

from core.models import Category, Book, Progress, Review

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = "test"
    password = "test"
    is_staff = True
    is_superuser = True

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    title = 'x'

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = 'x'
    category = factory.SubFactory(CategoryFactory)


class ProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Progress
    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
    comment = 'x'
    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)


######################################## userAuths app ########################################################
from userAuths.models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
    email = 'x'
    username = 'x'
    