# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from services.models import ServicesPage, Service

class ServicesPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServicesPage, ServicesPageAdmin)