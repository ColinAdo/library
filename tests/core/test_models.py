import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_return(self, category_factory):
        category = category_factory(title="Test Category")
        assert category.__str__() == "Test Category"