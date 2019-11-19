from django import forms

from examination.models import CourseCourse


class CourseCreationForm(forms.ModelForm):
    
    class Meta:
        model = CourseCourse
        fields =  ['course_name', 'teacher', 'student']

class AddExamToCourseForm(forms.ModelForm):
    class Meta:
        model = CourseCourse
        fields = ['course_exam',]

