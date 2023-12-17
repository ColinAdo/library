import pytest

from userAuths.forms import RegisterForm, ProfileFrom


@pytest.mark.django_db
class TestRegisterForm:
    def test_register_form_valid(self):
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        form = RegisterForm(data=data)
        assert form.is_valid()

    def test_register_form_errors(self):
        data = {
            'username': '',
            'email': 'x',
        }
        form = RegisterForm(data=data)

        assert 'username' in form.errors
        assert 'email' in form.errors
        assert 'This field is required.' in form.errors['username']
        assert 'Enter a valid email address.' in form.errors['email']

    def test_password_not_match(self):
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'test',
            'password2': 'testpassword',
        }

        form = RegisterForm(data=data)
        assert form.data['password1'] != form.data['password2']
        
@pytest.mark.django_db
class TestProfileForm:
    def test_profile_form_valid(self):

        """
        Here the data muct correspond to the actual choices defined in the models.py 
        for career and choices else the test will fail 
        """
        data = {
            'profile_pic': 'profile',
            'career': 'teacher',
            'location': 'Nairobi, Kenya',
        }

        form = ProfileFrom(data=data)
        if not form.is_valid():
            print(form.errors)

        assert form.is_valid()

    def test_invalid_choices(self):
        data = {
            'career': 'Teacher',
            'location': 'nairobi, Kenya',
        }
        form = ProfileFrom(data=data)
        assert 'career' in form.errors
        assert 'location' in form.errors
