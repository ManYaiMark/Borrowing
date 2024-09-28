from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
  gender_choices = (
    ('M', 'Male'), 
    ('F', 'Female'),
    ('O', 'Other')
  )
  gender = models.CharField(max_length=1,choices=gender_choices,blank=True,null=True)
  age = models.PositiveBigIntegerField(blank=True,null=True)
  student_id = models.CharField(max_length=15,unique=True,blank=True,null=True)
  faculty = models.CharField(max_length=100,blank=True,null=True)
  phone_number = models.CharField(max_length=15,blank=True,null=True)
  


