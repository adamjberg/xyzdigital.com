# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from singleton.models import SingletonModel


class HomePage(SingletonModel):
    poster = models.ImageField(null=True, blank=True, upload_to='home/')
    mp4 = models.FileField(null=True, blank=True, upload_to='home/')
