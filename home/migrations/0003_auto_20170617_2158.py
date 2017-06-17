# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170609_0544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='video',
        ),
        migrations.AddField(
            model_name='homepage',
            name='mp4',
            field=models.FileField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
    ]