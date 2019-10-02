from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
#All things related to user logging in. Login, Account Creation, ect.


#Unused. Django handles this.
def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form':form})    
