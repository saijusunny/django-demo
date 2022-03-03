from ntpath import join
from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=225)
    fee = models.IntegerField()

class student(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    std_name=models.CharField(max_length=255)
    std_address=models.CharField(max_length=255)
    std_age =models.IntegerField()
    join_date=models.DateField()
