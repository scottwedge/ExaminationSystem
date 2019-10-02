from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.Field(required=True, label='First Name')
    lastname = forms.Field(required=True, label='Last Name')

    class Meta:
        model = User
        fields = ['username', 'email','firstname', 'lastname', 'password1', 'password2']