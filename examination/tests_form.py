import datetime
from django import forms
from .models import exam
from django.test import TestCase
from django.utils import timezone
from examination.forms import addExam

class TestExamForm(TestCase):
    def test_StartExamForm(self):
        form = addExam()
        self.assertFalse(form.is_valid())

    def test_MultipleChoiceCheckFormFields(self):
        form = addExam()
        self.assertTrue(form.fields['title'].label == None or form.fields['title'].label == 'Title')
        self.assertTrue(form.fields['question'].label == None or form.fields['question'].label == 'Question')
        self.assertTrue(form.fields['option1'].label == None or form.fields['option1'].label == 'Option1')
        self.assertTrue(form.fields['option2'].label == None or form.fields['option2'].label == 'Option2')
        self.assertTrue(form.fields['option3'].label == None or form.fields['option3'].label == 'Option3')
        self.assertTrue(form.fields['option4'].label == None or form.fields['option4'].label == 'Option4')
        self.assertTrue(form.fields['correct'].label == None or form.fields['correct'].label == 'Correct')
    
    
