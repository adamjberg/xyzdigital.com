# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_teampage'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='titleExtra',
            field=models.TextField(null=True, blank=True),
        ),
    ]
