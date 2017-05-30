# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 11:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('YAVP', '0004_auto_20170530_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=170)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=170)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAVP.Country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='Continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAVP.Continent'),
        ),
        migrations.AddField(
            model_name='district',
            name='City',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YAVP.City'),
        ),
        migrations.AddField(
            model_name='area',
            name='Country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='YAVP.Country'),
        ),
    ]
