# Generated by Django 2.2.10 on 2020-02-10 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_round', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_id', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_no', models.IntegerField()),
                ('player_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('text', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Event')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Judge')),
                ('penalty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Penalty')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Player')),
                ('violation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='penaltylogger.Violation')),
            ],
        ),
    ]
