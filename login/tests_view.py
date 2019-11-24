from django.test import TestCase
from django.test import TestCase
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm, UserUpdateForm 
from user.forms import ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

class AllTasksViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                                         password='12test12',
                                                         email='test@example.com')
        self.user.save()
        self.timestamp = datetime.date.today()
        self.client.login(username='test', password='12test12')

    def tearDown(self):
        self.user.delete()

   # def test_login_view(self):
   #     url = reverse('login')
   #     response = self.client.get(url)
   #     self.assertEqual(response.status_code, 200)
   #     self.assertTemplateUsed(response, 'login.html')
   #     self.assertIsNotNone(self.client.login)

    def testregister_view(self):
       
            form =  UserRegisterForm()
            self.assertTrue(form.is_valid)
           # self.assertIsNotNone(form..get('username'))
            
         # return render(request, 'registration/register.html', {'form':form})    

  