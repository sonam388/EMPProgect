from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    salary = models.IntegerField()

def __str__(self):
    return self.name
