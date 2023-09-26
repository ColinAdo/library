from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'Placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomFileInput(ClearableFileInput):
    initial_text = _('') 
    input_text = _('Change')
    clear_checkbox_label = ''

class ProfileFrom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic', 'career', 'location']
        