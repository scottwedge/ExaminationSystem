from django.db import models
import datetime


# Create your models here.
class Login(models.Model):
    username         = models.CharField(max_length=40) #max_length = required
    password         = models.CharField(max_length=40)
