# Generated by Django 5.2.1 on 2025-06-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trattamento',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
