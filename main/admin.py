from django.contrib import admin
from .models import Animal, Breed, Event

admin.site.register(Breed)
admin.site.register(Animal)
admin.site.register(Event)

