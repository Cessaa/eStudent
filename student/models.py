from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse


# Create your models here.

class Student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999)],
                                             verbose_name="Student ID")
    firstName = models.CharField(max_length=20, verbose_name="First Name")
    lastName = models.CharField(max_length=30, verbose_name="Last Name")
    department = models.CharField(max_length=50, verbose_name="Department")
    mathScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Math Score")
    physicsScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Physics Score")
    chemistryScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Chemistry Score")
    biologyScore = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name="Biology Score")

    def __str__(self):
        return self.firstName + " " + self.lastName

    def get_edit_absolute_url(self):
        return reverse("student:edit", kwargs={"id": self.student_id})

    def get_delete_absolute_url(self):
        return reverse("student:delete", kwargs={"id": self.student_id})

    def testing_model(self):
        fllName = self.firstName + " " + self.lastName
        ort = (self.mathScore + self.physicsScore + self.chemistryScore + self.biologyScore) / 4
        return fllName + " " + str(ort)
