from django.contrib import admin
from .models import Animal, Breed, Farm

admin.site.register(Breed)
admin.site.register(Farm)
admin.site.register(Animal)

