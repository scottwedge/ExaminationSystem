from django.db import models

# Create your models here.
class tests(models.Model):
	title = models.CharField(max_length=200)
	question = models.CharField(max_length=200)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	correct = models.CharField(max_length=100)
	def __str__(self):
		return f'{self.title} tests'