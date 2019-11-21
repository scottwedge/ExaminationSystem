import datetime
from django import forms
from .models import exam, MultipleChoice, CourseCourse
from django.test import TestCase
from django.utils import timezone
from examination.forms import addExam, exam
 

class TestModel(TestCase):
  
    def test_MultipleChoiceModelExam(self):
        entry = exam(title="My entry title")
        self.assertEqual(str(entry), entry.title)

    def test_MultipleChoiceModel(self):

        questionname = MultipleChoice(question_name="My Question name")
        self.assertEqual(str(questionname), questionname.question_name)

    def testCourseCourse(self):
        coursename =  CourseCourse(course_name="the course")
        self.assertEqual(str(coursename), coursename.course_name)
   
     
    
