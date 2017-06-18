# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from page.models import Page


class ServicesPage(Page):
    pass


class Service(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
