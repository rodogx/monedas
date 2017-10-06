# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monedas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('abreviacion', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paridades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('paridad', models.DecimalField(decimal_places=4, max_digits=10)),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Monedas')),
            ],
        ),
    ]
