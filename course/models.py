from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(default='Null_Course', max_length=50)
    teacher = models.CharField(default='add in later', max_length=50)

    def __str__(self):
        return f'{self.course_name}'
        