from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

