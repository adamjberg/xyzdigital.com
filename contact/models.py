# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from singleton.models import SingletonModel
from header.models import Header


class ContactPage(SingletonModel):
    header = models.ForeignKey(Header, null=True, blank=True,)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()