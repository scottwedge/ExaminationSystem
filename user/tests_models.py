from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
import os


class TestUserModel(TestCase):
    @classmethod
    #def setUpTestData(self):
      
        
   #def test_return_value(self):
    #    user = User.objects.get(id=1)
     #   expected_return_value = '{} {}'.format(user.first_name, user.last_name)
      #  self.assertEquals(expected_return_value, str(user))

    
    
    def testUserData(self):
        self.profile1 = User.objects.create(id=1, first_name='Colleen', 
                       last_name='Rooney', email='cmrooney@uno.edu')

    def test_true(self):

        self.assertEquals(self.profile1.first_name, 'Colleen')
        self.assertEquals(self.profile1.last_name, 'Rooney')
        self.assertEquals(self.profile1.email, 'cmrooney@uno.edu')
   

    def test_false(self):
        self.assertNotEquals(self.profile1.first_name, 'John')
        self.assertNotEquals(self.profile1.last_name, 'John')
        self.assertNotEquals(self.profile1.email, 'John')
      #  class WhateverTest(TestCase):

    
    #   user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #role = models.CharField(default='S', max_length=1)
    #country = models.CharField(default = 'United States', max_length=40, blank = True)
    #state = models.CharField(default='Louisiana', max_length=40, blank = True)
    #city = models.CharField(default='New Orleans', max_length=40, blank = True)
    #bio = models.CharField(default="Enter a Bio", max_length=200, blank=True, null=True)