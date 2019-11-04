from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.class 
class exam(models.Model):
	#questions = models.ManyToManyField(MultipleChoice)
    title = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        managed = True
        db_table = 'exam'
	#def __str__(self):
	#	return f'{self.title} exam'

class MultipleChoice(models.Model):
    #mc_id = models.IntegerField(primary_key=True)
    exam_name = models.ForeignKey('exam', on_delete=models.CASCADE)
    question_name = models.TextField(blank=True, null=True)
    answer1 = models.TextField(blank=True, null=True)
    answer2 = models.TextField(blank=True, null=True)
    answer3 = models.TextField(blank=True, null=True)
    answer4 = models.TextField(blank=True, null=True)
    correct_answer = models.TextField(blank=True, null=True)
    #question_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multiple_choice'




class CourseCourse(models.Model):
    course_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ManyToManyField(User,related_name='+')
    course_exam = models.ManyToManyField('exam')
    class Meta:
        managed = True
        db_table = 'my_course'

    #def __str__(self):
    #    return f'{self.course_name}'


""" class Exam(models.Model):
    exam_id = models.IntegerField(primary_key=True)
    exam_name = models.TextField(blank=True, null=True)
    exam_type_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    exam_question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam'


class ExamQuestion(models.Model):
    exam_question_id = models.IntegerField(primary_key=True)
    exam_type_id = models.IntegerField(blank=True, null=True)
    mc_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question'


class ExamResults(models.Model):
    exam_results_id = models.IntegerField(primary_key=True)
    exam_results = models.TextField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_results'


class ExamType(models.Model):
    exam_type_id = models.IntegerField(primary_key=True)
    exam_type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_type'


class ExaminationQuestion(models.Model):
    dummy = models.CharField(max_length=50)
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination_question'





class QuestionType(models.Model):
    question_type_id = models.IntegerField(primary_key=True)
    question_type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_type'


"""
# Unable to inspect table 'student_answers'
# The error was: permission denied for relation student_answers

# Unable to inspect table 'students'
# The error was: permission denied for relation students

# Unable to inspect table 'teachers'
# The error was: permission denied for relation teachers

