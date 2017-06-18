from django.contrib import admin
from header.models import Header

class HeaderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Header, HeaderAdmin)
