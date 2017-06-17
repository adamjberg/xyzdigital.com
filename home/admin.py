# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import HomePage

# Register your models here.


class HomePageAdmin(admin.ModelAdmin):
    pass


admin.site.register(HomePage, HomePageAdmin)
