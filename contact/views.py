# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from contact.models import ContactPage
from contact.forms import ContactForm


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["contact"] = ContactPage.load()
        return context

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)
