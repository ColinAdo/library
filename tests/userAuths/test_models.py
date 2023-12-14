import pytest

pytestmark = pytest.mark.django_db

class TestCustomUserModel:
    def test_str_return(self, custom_user_factory):
        user = custom_user_factory(username="Test User")

        assert user.__str__() == "Test User"