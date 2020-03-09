from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Student(models.Model):
     student_id = models.PositiveIntegerField(primary_key = True, validators=[MaxValueValidator(9999)], verbose_name="Student ID")
     firstName = models.CharField(max_length=20, verbose_name="First Name")
     lastName = models.CharField(max_length=30, verbose_name="Last Name")
     department = models.CharField(max_length=50, verbose_name="Department")
     mathScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Math Score")
     physicsScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Physics Score")
     chemistryScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Chemistry Score")
     biologyScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Biology Score")

     def __str__(self):
         return self.student_id
     