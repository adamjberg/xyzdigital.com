# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_teampage_titleextra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teampage',
            old_name='titleExtra',
            new_name='title_extra',
        ),
    ]
