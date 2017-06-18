# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20170617_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
