from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField
from datetime import datetime, date


# Create your models here.
class Register(AbstractUser):
    is_admin = BooleanField(default="False")
    is_student = BooleanField(default="False")

class Admin(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)


class Student(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    contact_number = models.CharField(max_length=10)
    photo = models.FileField(upload_to='documents/')

    def __str__(self):
        return f'{self.name}'

    def calculate_age(self):
        today = date.today()
        birth_date = self.dob
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

class Marks(models.Model):
    name = models.ForeignKey('Student',on_delete=models.DO_NOTHING)
    english = models.CharField(max_length=5)
    maths = models.CharField(max_length=5)
    science = models.CharField(max_length=5)