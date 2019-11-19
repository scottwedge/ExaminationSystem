from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from login.forms import UserUpdateForm
from user.forms import ProfileUpdateForm
from user.models import Profile
from django.utils import timezone
from django.test import TestCase
from examination.models import CourseCourse, exam, MultipleChoice
from django.urls import reverse


@login_required
def teststudent_view(self):
	
    #self.assertTrue(self.user.profile.role == 'S')
    self.assertTrue(studentCourses = self.student) 
   # self.asertFalse(self.user.profile.role == 'T')

@login_required
def testchangeprofile_view(self):  
    a_form = UserUpdateForm(self.user)
    self.assertTrue(a_form.is_valid)
   
  

@login_required
def testprofile_view(self):
    self.assertTrue(self.user.profile.is_valid)
   # self.asertFalse(self.user.profile.role == 'T')
    url = reverse('profile')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

@login_required
def testgrades_view(self):
   
    url = reverse('grade')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
 


@login_required
def testagile(self):
    #self.assertTrue( self.user.profile.role.student == CourseCourse.student) 
    #self.assertFalse( self.user.profile.role.student == CourseCourse.teacher)
    url = reverse('ag')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    #self.assertTemplateUsed(response, 'ag.html')
   # self.assertContains(response, 'ag')
 
@login_required
def testcourse_exams_view(self):
    url = reverse('course_exams')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

@login_required
def testcourse_grades_view(self):
    url = reverse('course_grades')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
