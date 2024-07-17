from django.db import models

# Create your models here.:
class Student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    img=models.FileField(upload_to='images/')

