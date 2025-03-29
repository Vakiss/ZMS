from django import forms
from .models import Animal, Event

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['number', 'gender', 'color', 'name', 'weight']
        labels = {
            'number': 'Number',
            'gender': 'Gender',
            'color': 'Color',
            'name': 'Name',
            'weight': 'Weight',
            'birth_date': 'Birth Date',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_number(self):
        data = self.cleaned_data['number'].strip()
        data = data.upper()
        if not data.startswith('LT'):
            data = 'LT' + data
        return data

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type', 'date', 'notes']
        labels = {
            'event_type': 'Event type',
            'date': 'Event date',
            'notes': 'Notes',
        }