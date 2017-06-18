# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from page.models import Page


class TeamPage(Page):
    pass


class Member(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(null=True, blank=True, max_length=20)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="team/")
