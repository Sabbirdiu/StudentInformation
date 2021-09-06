from django.db import models


# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'))
    stu_id = models.CharField(max_length=50, unique=True,error_messages={'unique':"this Student id is already exists"})
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex =  models.CharField(max_length=50, choices=GENDER_CHOICES)
    father_Name = models.CharField(max_length=50)
    mother_Name = models.CharField(max_length=50)
    last_Education = models.CharField(max_length=50)
    def __str__(self):
        return self.name

 