# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('qotat_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.Quotation'),
        ),
    ]
