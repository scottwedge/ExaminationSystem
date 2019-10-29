from django.contrib import admin
from .models import CourseCourse
from .models import exam
from django.contrib.auth.models import User
# Register your models here.


#Admin control for the CourseCourse model to allow editing of student list.
class CourseAdmin(admin.ModelAdmin):
    model = CourseCourse
    filter_horizontal = ('student',)

admin.site.register(CourseCourse,CourseAdmin)
admin.site.register(exam)


