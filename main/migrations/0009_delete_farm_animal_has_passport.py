# Generated by Django 5.1.7 on 2025-03-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_animal_mother'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Farm',
        ),
        migrations.AddField(
            model_name='animal',
            name='has_passport',
            field=models.BooleanField(default=False),
        ),
    ]
