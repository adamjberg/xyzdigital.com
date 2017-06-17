# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from singleton.models import SingletonModel

# Create your models here.


class HomePage(SingletonModel):
    poster = models.ImageField(null=True, blank=True, upload_to='home/')
    mp4 = models.FileField(null=True, blank=True, upload_to='home/')
