# Generated by Django 4.0.5 on 2022-06-23 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='team',
            new_name='teams',
        ),
    ]
