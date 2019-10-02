"""djProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView 
from homepage.views import student_view, logout_view, profile_view, grades_view, agile_test
from login.views import login_view, register_view

urlpatterns = [
    #Admin View
    path('admin/', admin.site.urls),

    #Login views
    path('', LoginView.as_view(), name='login'), #third try.
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),    
    path('register/', register_view, name='register'), 

    #Homepage Views
    path('homepage/', student_view, name='student_logged_in'),
    path('profile/', profile_view),
    path('grades/', grades_view),
    path('ag/', agile_test),
]
