# Generated by Django 4.0 on 2023-10-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
