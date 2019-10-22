from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm, UserUpdateForm 
from user.forms import ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
#All things related to user logging in. Login, Account Creation, ect.

import logging
logger = logging.getLogger(__name__)
#Unused. Django handles this.
def login_view(request, *args, **kwargs):
    logger.info('Someone accessed the Login view')
    return render(request, "login.html", {})


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        logger.info('Someone accessed the Registration view')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form':form})    
