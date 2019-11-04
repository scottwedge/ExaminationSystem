import datetime

from django.test import TestCase
from django.utils import timezone
from login.forms import UserRegisterForm

class TestLoginForm(TestCase):
    def test_StartLoginForm(self):
        form = UserRegisterForm()
        self.assertFalse(form.is_valid())
     
    def test_LoginCheckFormFields(self):
        form = UserRegisterForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'First Name')
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Last Name')
 