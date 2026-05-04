from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    address  =models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
    
