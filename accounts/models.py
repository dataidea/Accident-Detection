from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    
class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures', blank=True, null=True)
    notifications = models.ManyToManyField(Notification)

    def __str__(self):
        return self.username