from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100,choices=settings.PAGE_TITLES)
    subject = models.CharField(max_length=100,blank=True,null=True,
                        choices=settings.PAGE_SUBJECTS)
    language_code = models.CharField(max_length=2,choices=settings.LANGUAGES)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.title,self.subject)
