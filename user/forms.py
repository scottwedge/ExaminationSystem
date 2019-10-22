from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    country = forms.CharField(required=False, label='Country')
    state = forms.CharField(required=False, label='State')
    city = forms.CharField(required=False, label='City')
    bio =  forms.CharField(required=False, label='Bio')

    class Meta:
        model = Profile
        fields = ('country','image','state','city','bio')