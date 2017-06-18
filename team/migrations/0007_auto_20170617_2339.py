# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
        ('team', '0006_auto_20170617_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='title_extra',
        ),
        migrations.AddField(
            model_name='teampage',
            name='header',
            field=models.ForeignKey(blank=True, to='header.HeaderModel', null=True),
        ),
    ]
