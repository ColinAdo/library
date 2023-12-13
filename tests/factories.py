import factory

from django.contrib.auth.models import User

from core.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = "x"
        