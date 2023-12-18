from django.test import RequestFactory
from core.context_processor import default

import pytest

pytestmark = pytest.mark.django_db

class TestContextProcessor:
    def test_default_return_none(self):

        factory = RequestFactory()
        request = factory.get('/')
        request.user = None

        response = default(request)

        assert response['p'] is None

    def test_default_not_none(self, category_factory, custom_user_factory):
        user = custom_user_factory(username="Test User")
        category = category_factory(title="Test Category")

        factory = RequestFactory()
        request = factory.get('/')
        request.user = user

        response = default(request)

        assert 'categories' in response
        assert 'p' in response
        assert response['categories'].count() == 1
        assert response['p'] == request.user
