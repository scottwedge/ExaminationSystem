from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(default='S', max_length=1)
    country = models.CharField(default = 'United States', max_length=40, blank = True)
    state = models.CharField(default='Louisiana', max_length=40, blank = True)
    city = models.CharField(default='New Orleans', max_length=40, blank = True)
    bio = models.CharField(default="Enter a Bio", max_length=200, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'