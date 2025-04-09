# Galvijų Informacinė Sistema
![Sistema logo](galvijai_project/static/images/cow.jpg)


Ši sistema skirta valdyti gyvulių duomenis, įvykius, pasų užsakymus, ataskaitas ir kitus ūkio procesus.

## Reikalavimai

- Python  
- Django (5.x – patikrinkite `requirements.txt` failą)  
- Kitos priklausomybės nurodytos faile [requirements.txt](requirements.txt)

# Sukurkite ir aktyvuokite virtualią aplinką:

Windows:
`python -m venv venv`

`venv\Scripts\activate`

macOS/Linux:
`python3 -m venv venv`

`source venv/bin/activate`

# Įdiekite reikalavimus:
`pip install -r requirements.txt`

# Atlikite duomenų bazės migracijas:
`python manage.py makemigrations`

`python manage.py migrate`

# Sukurkite supervartotoją:
`python manage.py createsuperuser`

# Paleiskite Django serverį:
`python manage.py runserver`

