from django.db import models

from singleton.models import SingletonModel
from header.models import Header


class Page(SingletonModel):
    header = models.ForeignKey(Header, null=True, blank=True)

    class Meta:
        abstract = True
