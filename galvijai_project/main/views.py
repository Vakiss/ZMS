from django.shortcuts import render, get_object_or_404
from .models import Animal

def index(request):
    return render(request, 'main/index.html')

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'main/animal_list.html', {'animals': animals})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'main/animal_detail.html', {'animal': animal})
