from django.db import models



class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Farm(models.Model):
    naame = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField(blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='animals')

    def __str__(self):
        return f"{self.name} ({self.breed})"