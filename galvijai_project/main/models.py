from django.db import models



class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Farm(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    number = models.CharField(max_length=14,null=True, blank=True,unique=True)
    gender = models.CharField(max_length=10,null=True, blank=True, choices=[('male', 'Male'), ('female', 'Female')])
    color = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.gender})"