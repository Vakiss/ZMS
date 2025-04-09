from django import forms
from .models import Animal, GENDER_CHOICES, COLOR_CHOICES, EVENT_TYPE_CHOICES

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


class SpecialEventForm(forms.Form):
    event_type = forms.ChoiceField(choices=EVENT_TYPE_CHOICES)
    date = forms.DateField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    # Laukai naujam gyvuliui
    child_name = forms.CharField(required=False)
    child_number = forms.CharField(required=False,max_length=14)
    child_gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False
    )
    child_color = forms.ChoiceField(
        choices=COLOR_CHOICES,
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        event_type = cleaned_data.get('event_type')
        child_number = cleaned_data.get('child_number')

        if event_type == 'prieauglio_atsivedimas':
            # Tikriname, ar vartotojas užpildė privalomus duomenis
            if not child_number:
                self.add_error('child_number', 'Privaloma nurodyti naujo gyvulio numerį.')
        return cleaned_data