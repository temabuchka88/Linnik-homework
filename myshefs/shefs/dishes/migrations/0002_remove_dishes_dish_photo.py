# Generated by Django 5.0.1 on 2024-02-19 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='dish_photo',
        ),
    ]
