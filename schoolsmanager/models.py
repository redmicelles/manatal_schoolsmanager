from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class School(models.Model):

    """School Schema Definition"""
    schoolname = models.CharField(max_length=20, null=False, verbose_name="School Name", unique=True)
    maxstudents = models.IntegerField(validators = [MinValueValidator(1)], verbose_name="Maximum Number of Students Allowed")

    def __str__(self):

        return self.schoolname
    class Meta:
        
        ordering = ["schoolname"]
        verbose_name = "Schools Schema"

class Student(models.Model):

    """Student Schema Definition"""
    firstname = models.CharField(max_length=20, null=False, verbose_name="First Name")
    lastname = models.CharField(max_length=20, verbose_name="Last Name")
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False)
    student_id = models.CharField(max_length=20, null=False, unique=True)
    age = models.IntegerField(verbose_name="Student's Age", default=0)
    nationality = models.CharField(max_length=20, verbose_name="Nationality", default="")

    def __str__(self):

        return f"{self.firstname} {self.lastname}"


    class Meta:

        ordering = ["firstname"]
        verbose_name = "Students Schema"