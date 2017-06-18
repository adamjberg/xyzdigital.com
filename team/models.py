# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from singleton.models import SingletonModel
from header.models import Header


class TeamPage(SingletonModel):
    header = models.ForeignKey(Header, null=True, blank=True,)


class Member(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(null=True, blank=True, max_length=20)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="team/")
