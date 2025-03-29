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
    numeris = models.CharField(max_length=50,null=True, blank=True,unique=True)
    lytis = models.CharField(max_length=10,null=True, blank=True, choices=[('patinas', 'Patinas'), ('patelė', 'Patelė')])
    spalva = models.CharField(max_length=50, blank=True, null=True)
    vardas = models.CharField(max_length=50, blank=True, null=True)
    svoris = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.vardas} ({self.lytis})"