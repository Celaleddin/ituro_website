from __future__ import unicode_literals
from page.models import Page
from gallery.models import Gallery
from team.models import Team
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models


def get_image_upload_path(instance,filename):
    return "sponsors/{}/{}".format(instance.name,filename)


def get_document_upload_path(instance,filename):
    return "documents/{}/{}".format(instance.page,filename)


class CommonEntry(models.Model):
    title = models.CharField(max_length=100)
    page = models.ForeignKey(Page)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CategoryEntry(models.Model):
    page = models.ForeignKey(Page)
    document = models.FileField()
    gallery = models.ForeignKey(Gallery)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page

class NewsEntry(models.Model):
    title = models.CharField(max_length=100)
    page = models.ForeignKey(Page)
    content = RichTextField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LinkEntry(models.Model):
    page = models.ForeignKey(Page)
    name = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamEntry(models.Model):
    page = models.ForeignKey(Page)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Team")

    def __str__(self):
        return self.name

class SponsorEntry(models.Model):
    page = models.ForeignKey(Page)
    name = models.CharField(max_length=100)
    sponsor_type = models.CharField(max_length=100,choices=settings.SPONSOR_TYPES)
    logo = models.ImageField(upload_to=get_image_upload_path)
    url = models.URLField()
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = _("Sponsor")

    def __str__(self):
        return self.name

class GalleryEntry(models.Model):
    page = models.ForeignKey(Page)
    gallery = models.ForeignKey(Gallery)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery

@receiver(pre_save,sender=NewsEntry)
def NewsEntry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)
