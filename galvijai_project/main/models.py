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


COLOR_CHOICES = [
    ('grey', '1 - Grey'),
    ('brown', '2 - Brown'),
    ('black', '3 - Black'),
    ('white', '4 - White'),
    ('spotted', '5 - Spotted'),
    ('yellow', '6 - Yellow'),
    ('mottled', '7 - Mottled'),
    ('light_grey', '8 - Light Grey'),
    ('cream', '9 - Cream'),
    ('golden', '10 - Golden'),
    ('red', '11 - Red'),
]

class Animal(models.Model):
    number = models.CharField(max_length=14,null=True, blank=True,unique=True)
    gender = models.CharField(max_length=10,null=True, blank=True, choices=[('male', 'Male'), ('female', 'Female')])
    color = models.CharField(max_length=50,choices=COLOR_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.gender})"