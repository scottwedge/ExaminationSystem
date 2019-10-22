from django.db import models
from course.models import Course
import logging
logger = logging.getLogger(__name__)

# Create your models here.
class Question(models.Model):
    dummy = models.CharField(default=None, max_length=50)
    
    ##THIS IS WHERE THE WORK BEGINS
    #this is a guess...
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    logger.info('Examination Models touched')


    #chapter 
    #question_text
    #one-to-one mkmigr
    
    
    
    #num_answers
    #correct_answer
    #answer_1
    #answer_2
    #answer_3
    #answer_4
    #answer_5

    def __str__(self):
        return f'{self.dummy}'
        #,self.course
