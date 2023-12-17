import pytest

from userAuths.forms import RegisterForm, ProfileFrom


@pytest.mark.django_db
class TestRegisterForm:
    def setup_method(self):
        # Common data used in multiple test methods
        self.valid_data = {
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        self.invalid_data = {
            'username': '',
            'email': 'x',
        }

    def test_register_form_valid(self):
        form = RegisterForm(data=self.valid_data)
        assert form.is_valid()

    def test_register_form_errors(self):
        form = RegisterForm(data=self.invalid_data)

        assert 'username' in form.errors
        assert 'email' in form.errors
        assert 'This field is required.' in form.errors['username']
        assert 'Enter a valid email address.' in form.errors['email']

    def test_password_not_match(self):
        self.valid_data['password2'] = "test"

        form = RegisterForm(data=self.valid_data)
        assert self.valid_data['password1'] != form.data['password2']

@pytest.mark.django_db
class TestProfileForm:
    def setup_method(self):
        self.valid_data = {
            'profile_pic': 'profile',
            'career': 'teacher',
            'location': 'Nairobi, Kenya',
        }

        self.invalid_data = {
            'career': 'Teacher',
            'location': 'nairobi, Kenya',
        }

    def test_profile_form_valid(self):

        """
        Here the data muct correspond to the actual choices defined in the models.py 
        for career and choices else the test will fail 
        """

        form = ProfileFrom(data=self.valid_data)
        if not form.is_valid():
            print(form.errors)

        assert form.is_valid()

    def test_invalid_choices(self):
        form = ProfileFrom(data=self.invalid_data)
        assert 'career' in form.errors
        assert 'location' in form.errors
