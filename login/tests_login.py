from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase

class TestLogIn(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        print("setUp: Add user and password to self.credentials")
        User.objects.create_user(**self.credentials)
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_login_True(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        print("Logging In")
        self.assertTrue(response)
