# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from stories.models import StoriesPage, Story

class StoriesPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoriesPage, StoriesPageAdmin)

class StoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Story, StoryAdmin)