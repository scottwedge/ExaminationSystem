import datetime
from django import forms
from .models import exam, MultipleChoice
from django.test import TestCase
from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import addExam, examUpdate
from .models import exam
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import add_exam, edit_exam, exam_detail
from .forms import exam, addExam, examUpdate
 

class TestView(TestCase):
  
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def testaddexam(self):
        request = self.factory.get('/add_exam')
        request.user = self.user
        request.user = AnonymousUser()
        response = add_exam(request)
        self.assertEqual(response.status_code, 200)

    def testexam_detail(self):
        request = self.factory.get('/exam_detail')
        request.user = self.user
        request.user = AnonymousUser()
        response = add_exam(request)
        self.assertEqual(response.status_code, 200)

    def testeditexam(self):
        request = self.factory.get('/add_exam')
        request.user = self.user
        request.user = AnonymousUser()
        response = add_exam(request)
        self.assertEqual(response.status_code, 200)

   # def testexamform(self):
        #form = addExam(request.POST)
	    #self.assertTrue(form.is_valid)
    #    form = add_exam(self)
    #    self.assertTrue(form.is_valid)
		
	
