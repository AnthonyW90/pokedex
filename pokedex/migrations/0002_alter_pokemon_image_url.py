# Generated by Django 4.2 on 2023-06-12 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
