from django import forms
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