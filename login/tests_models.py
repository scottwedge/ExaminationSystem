from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models

class TestLoginModel(TestCase):
    @classmethod
    def testLoginData(cls):
     
            username = models.CharField(max_length=40) #max_length = required
            password = models.CharField(max_length=40)

      
   # def get_absolute_url(self):
   #     return reverse('TestLoginModel-detail', args=[str(self.id)])
    
   # def __str__(self):
   #     return f'{self.username}, {self.password}'
   