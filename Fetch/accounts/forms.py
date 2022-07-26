from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "E-mail...",
        "class": "form-control",
        "type": "text"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password...",
        "class": "form-control",
        "type": "password"}))
