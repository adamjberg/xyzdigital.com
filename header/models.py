from django.db import models


class Header(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='header/')
    title = models.CharField(null=True, blank=True, max_length=20)
    extra = models.TextField(null=True, blank=True)