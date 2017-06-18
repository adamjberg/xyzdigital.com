# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView
from services.models import ServicesPage


class ServicesView(TemplateView):
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context["header"] = ServicesPage.load().header
        return context
