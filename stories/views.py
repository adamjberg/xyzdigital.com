# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from stories.models import StoriesPage, Story


class StoriesView(TemplateView):
    template_name = "stories/stories.html"

    def get_context_data(self, **kwargs):
        context = super(StoriesView, self).get_context_data(**kwargs)
        context["header"] = StoriesPage.load().header
        context["stories"] = Story.objects.all()
        return context
