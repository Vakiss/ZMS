# Generated by Django 5.1.7 on 2025-03-29 12:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_animal_birth_date_alter_animal_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('prieauglio_atsivedimas', 'Prieauglio atsivedimas'), ('gaisimas', 'Gaišimas'), ('isvezimas', 'Išvežimas')], max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='main.animal')),
            ],
        ),
    ]
