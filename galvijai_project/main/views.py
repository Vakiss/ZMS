from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm,SpecialEventForm
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db.models import Count, Q

def index(request):
    return render(request, 'main/index.html')

@login_required
def animal_list(request):
    animals = Animal.objects.filter(owner=request.user)
    return render(request, 'main/animal_list.html', {'animals': animals})





@login_required
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk, owner=request.user)
    events = animal.events.all().order_by('-date')
    return render(request, 'main/animal_detail.html', {'animal': animal, 'events': events})


def add_event(request, animal_id):
    mother = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = SpecialEventForm(request.POST)
        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            if event_type == 'Prieauglio atsivedimas' and mother.gender.lower() != 'female':
                form.add_error('event_type', 'Tik patelės gali turėti prieauglio atsivedimo įvykį.')
                return render(request, 'main/add_event.html', {'form': form, 'animal': mother})
            date = form.cleaned_data['date'] or timezone.now().date()
            notes = form.cleaned_data['notes']

            # 1) Sukuriame patį Event
            new_event = Event.objects.create(
                animal=mother,
                event_type=event_type,
                date=date,
                notes=notes
            )

            # 2) Jeigu tai prieauglio atsivedimas, sukuriame naują gyvulį
            if event_type == 'Prieauglio atsivedimas':
                child_name = form.cleaned_data['child_name']
                child_number = form.cleaned_data['child_number']
                child_color = form.cleaned_data['child_color']
                child_gender = form.cleaned_data['child_gender']
                Animal.objects.create(
                    name=child_name,
                    number=child_number,
                    mother=mother,
                    color= child_color,
                    gender = child_gender
                )

            return redirect('animal_detail', pk=mother.pk)
    else:
        form = SpecialEventForm()
    return render(request, 'main/add_event.html', {'form': form, 'animal': mother})




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
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'main/new_animal.html', {'form': form})





def passport(request):
    eligible_animals = Animal.objects.filter(has_passport=False) \
        .exclude(events__event_type__in=['Gaišimas', 'Išvežimas']).distinct()
    return render(request, 'main/pasai.html', {'animals': eligible_animals})

@require_POST
def order_passport(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    # Patikriname, ar gyvulis yra eligible
    if not animal.has_passport and not animal.events.filter(event_type__in=['Gaišimas', 'Išvežimas']).exists():
        animal.has_passport = True
        animal.save()
    return redirect('passport')

def ordered_passports(request):
    # Atrenkame gyvulius, kurių has_passport yra True
    ordered_animals = Animal.objects.filter(has_passport=True)
    return render(request, 'main/ordered_passports.html', {'animals': ordered_animals})


def isagai(request):
    eligible_animals = Animal.objects.filter(has_isagai=False) \
        .exclude(events__event_type__in=['Gaišimas', 'Išvežimas']).distinct()
    return render(request, 'main/isagai.html', {'animals': eligible_animals})

@require_POST
def order_isagai(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if not animal.has_isagai and not animal.events.filter(event_type__in=['Gaišimas', 'Išvežimas']).exists():
        animal.has_isagai = True
        animal.save()
    return redirect('isagai')

def ordered_isagai(request):
    ordered_animals = Animal.objects.filter(has_isagai=True)
    return render(request, 'main/ordered_isagai.html', {'animals': ordered_animals})


@login_required
def ataskaitos(request):
    user = request.user
    # 1) Gyvuliai pagal lytį – rodo tik number ir gender
    animals_by_gender = Animal.objects.filter(owner=user).only('number', 'gender').order_by('gender')

    # 2) Gyvuliai pagal spalvą – rodo tik number ir color
    animals_by_color = Animal.objects.filter(owner=user).only('number', 'color').order_by('color')

    # 3) Prieauglio atsivedimų skaičius kiekvienam gyvuliui
    #    Pavyzdžiui, norime sužinoti, kiek "Prieauglio atsivedimo" eventų turi kiekvienas gyvulys
    animals_with_birth_count = (Animal.objects
        .filter(owner=user)
        .annotate(birth_count=Count('events', filter=Q(events__event_type='Prieauglio atsivedimas')))
        .order_by('-birth_count')
    )
    # Kiekvienas Animal objektas dabar turės papildomą lauką 'birth_count'

    context = {
        'animals_by_gender': animals_by_gender,
        'animals_by_color': animals_by_color,
        'animals_with_birth_count': animals_with_birth_count,
    }
    return render(request, 'main/ataskaitos.html', context)