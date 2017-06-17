# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from team.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
