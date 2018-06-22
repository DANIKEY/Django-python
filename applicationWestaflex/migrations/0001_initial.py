# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-06 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnregistreProcedure',
            fields=[
                ('id_procedure', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.CharField(max_length=100)),
                ('pression', models.IntegerField()),
                ('duree', models.IntegerField()),
                ('marge', models.IntegerField()),
                ('diametre', models.IntegerField()),
                ('reference', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureSelectionnee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_procedure', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistiques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=20)),
                ('tube_defectueux', models.IntegerField()),
                ('tube_non_defectueux', models.IntegerField()),
            ],
        ),
    ]