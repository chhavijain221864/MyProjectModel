from django.db import models

# Create your models here.
class Student(models.Model):
    studid=models.IntegerField()
    studname=models.CharField(max_length=70)
    studmail=models.EmailField(max_length=70)
    studadd=models.CharField(max_length=40)
    comment=models.CharField(max_length=50,default="not available")
    