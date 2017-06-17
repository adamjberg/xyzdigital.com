# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from team.models import Member

class TeamView(TemplateView):
    template_name = "team/team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context
