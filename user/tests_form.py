import datetime

from django.test import TestCase
from django.utils import timezone
from user.forms import ProfileUpdateForm

class TestUserForm(TestCase):
    def test_StartLoginForm(self):
        form = ProfileUpdateForm()
        self.assertFalse(form.is_valid())
     
    def test_LoginCheckFormFields(self):
        form = ProfileUpdateForm()
        self.assertTrue(form.fields['country'].label == None or form.fields['country'].label == 'Country')
        self.assertTrue(form.fields['state'].label == None or form.fields['state'].label == 'State')
        self.assertTrue(form.fields['city'].label == None or form.fields['city'].label == 'City')
        self.assertTrue(form.fields['bio'].label == None or form.fields['bio'].label == 'Bio')
 