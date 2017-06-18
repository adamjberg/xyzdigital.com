# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_auto_20170617_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.ForeignKey(blank=True, to='header.Header', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
