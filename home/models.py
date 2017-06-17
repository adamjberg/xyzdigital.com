# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from singleton.models import SingletonModel

# Create your models here.


class HomePage(SingletonModel):
    video = models.URLField(null=True, blank=True)
