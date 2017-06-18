# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from contact.models import ContactPage, Contact


class ContactPageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactPage, ContactPageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


admin.site.register(Contact, ContactAdmin)
