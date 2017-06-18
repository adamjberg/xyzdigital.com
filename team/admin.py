# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from team.models import TeamPage, Member


class TeamPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(TeamPage, TeamPageAdmin)


class MemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
