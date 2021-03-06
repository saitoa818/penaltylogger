# Generated by Django 3.0.6 on 2020-05-12 03:34

from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'penaltylogger/fixture/view_judge.json', app_label='penaltylogger')

class Migration(migrations.Migration):

    dependencies = [
        ('penaltylogger', '0002_penalty'),
    ]

    operations = [
         migrations.RunPython(load_fixture),
    ]