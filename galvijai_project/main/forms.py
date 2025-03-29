from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['number', 'gender', 'color', 'name', 'weight']
        labels = {
            'numeris': 'Numeris',
            'lytis': 'Lytis',
            'spalva': 'Spalva',
            'vadas': 'Vadas',
            'svoris': 'Svoris',
        }

    def clean_number(self):
        data = self.cleaned_data['numeris'].strip()
        data = data.upper()
        if not data.startswith('LT'):
            data = 'LT' + data
        return data
