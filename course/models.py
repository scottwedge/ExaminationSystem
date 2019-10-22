from django.db import models
import logging
logger = logging.getLogger(__name__)
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(default='default', max_length=50)
    teacher = models.CharField(default='Newton', max_length=50)

    logger.info('Course Model touched')
    
    def __str__(self):
        return f'{self.course_name}'
        