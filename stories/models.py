# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from page.models import Page


class StoriesPage(Page):
    pass


class Story(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
