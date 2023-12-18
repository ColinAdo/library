from django.urls import reverse, resolve
from urllib.parse import quote
from django.contrib.auth import views as auth_views

import pytest

from userAuths.views import (
    sign_up,
    sign_in,
    sign_out,
    profile,
    setting
)

@pytest.fixture
def user(request, custom_user_factory):
    return custom_user_factory(username="Test user")

@pytest.mark.django_db
class TestUrls:
    def test_register_url(self):
        found = resolve('/user/register/')

        assert found.func == sign_up
        assert reverse('sign_up') == "/user/register/"

    def test_sign_in_url(self):
        found = resolve('/user/login/')

        assert found.func == sign_in
        assert reverse('sign_in') == "/user/login/"

    def test_sign_out_url(self):
        found = resolve('/user/logout/')

        assert found.func == sign_out
        assert reverse('sign_out') == "/user/logout/"

    def test_profile_url(self, user):
        found = resolve(f"/user/{user.username}/profile/")

        expected_url = f"/user/{quote(user.username)}/profile/"
        assert found.func == profile
        assert reverse('profile', args=[f"{user.username}"]) == expected_url

    def test_settings_url(self, user):
        found = resolve(f"/user/{user.username}/settings/")

        expected_url = f"/user/{quote(user.username)}/settings/"
        assert found.func == setting
        assert reverse('setting', args=[f"{user.username}"]) == expected_url

    def test_password_reset_url(self):
        url = reverse('password_reset')
        found = resolve(url)

        assert found.func.view_class == auth_views.PasswordResetView

    def test_password_reset_done_url(self):
        url = reverse('password_reset_done')
        found = resolve(url)

        assert found.func.view_class == auth_views.PasswordResetDoneView

    def test_password_reset_confirm_url(self):
        url = reverse('password_reset_confirm', args=["uidb64", "token"])
        found = resolve(url)

        assert found.func.view_class == auth_views.PasswordResetConfirmView

    def test_password_reset_complete_url(self):
        url = reverse('password_reset_complete')
        found = resolve(url)

        assert found.func.view_class == auth_views.PasswordResetCompleteView

    
        
