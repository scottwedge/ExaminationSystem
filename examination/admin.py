from django.contrib import admin
from .models import CourseCourse, exam, MultipleChoice, ExamGrade, PotentialAnswer

from django.contrib.auth.models import User
# Register your models here.

#Admin control for the CourseCourse model to allow editing of student list.
class CourseAdmin(admin.ModelAdmin):
    model = CourseCourse
    filter_horizontal = ('student','course_exam')
   
admin.site.register(CourseCourse,CourseAdmin)
admin.site.register(exam)
admin.site.register(MultipleChoice)
admin.site.register(ExamGrade)
admin.site.register(PotentialAnswer)

