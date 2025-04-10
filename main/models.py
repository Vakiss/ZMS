from django.db import models
from django.utils import timezone
from django.conf import settings



class Breed(models.Model):
    name = models.CharField(max_length=100)

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
GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

EVENT_TYPE_CHOICES = [
    ('Prieauglio atsivedimas', 'Prieauglio atsivedimas'),
    ('Gaišimas', 'Gaišimas'),
    ('Išvežimas', 'Išvežimas'),
]

class Animal(models.Model):
    number = models.CharField(max_length=14,null=True, blank=True,unique=True)
    gender = models.CharField(max_length=10,null=True, blank=True, choices=[('male', 'Male'), ('female', 'Female')])
    color = models.CharField(max_length=50,choices=COLOR_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    mother = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='offspring'
    )
    has_isagai = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.gender})"

    has_passport = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='animals',
        null=True, blank=True
    )

    @property
    def alert(self):
        return self.events.filter(event_type__in=['Gaišimas', 'Išvežimas']).exists()



class Event(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_event_type_display()} ({self.animal.number})"

