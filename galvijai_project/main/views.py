from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm,EventForm


def index(request):
    return render(request, 'main/index.html')

@login_required
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'main/animal_list.html', {'animals': animals})





@login_required
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    events = animal.events.all().order_by('-date')
    return render(request, 'main/animal_detail.html', {'animal': animal, 'events': events})

@login_required
def add_event(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.animal = animal
            new_event.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = EventForm()
    return render(request, 'main/add_event.html', {'form': form, 'animal': animal})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def new_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'main/new_animal.html', {'form': form})