from django.test import TestCase
from django.contrib.auth.models import User


class TestLogIn(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        print("setUp: Add user and password to self.credentials")
        User.objects.create_user(**self.credentials)
        self.assertTrue(User)

    def tearDown(self):
        self.credentials.clear
       

    def test_login_True(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        #print("Logging In")
        self.assertTrue(response)
