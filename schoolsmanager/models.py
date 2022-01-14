from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class School(models.Model):

    """"""
    schoolname = models.CharField(max_length=20, null=False, verbose_name="School Name")
    maxstudents = models.IntegerField(validators = [MinValueValidator(0)], verbose_name="Maximum Number of Students Allowed")

    class Meta:

        """"""
        ordering = ["schoolname"]
        verbose_name = "Schools Schema"

    def __str__(self):

        """"""
        return self.schoolname

class Student(models.Model):

    """"""
    firstname = models.CharField(max_length=20, null=False, verbose_name="First Name")
    lastname = models.CharField(max_length=20, verbose_name="Last Name")
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:

        """"""
        ordering = ["firstname"]
        verbose_name = "Students Schema"

    def __str__(self):

        """"""
        return f"{self.firstname} {self.lastname}"