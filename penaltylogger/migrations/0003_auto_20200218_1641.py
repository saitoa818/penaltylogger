# Generated by Django 2.2.10 on 2020-02-18 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penaltylogger', '0002_auto_20200214_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Player'),
        ),
    ]
