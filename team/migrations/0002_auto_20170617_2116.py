# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
