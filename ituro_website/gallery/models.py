from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=50,choices=settings.GALLERY_TITLES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


def get_upload_path(instance,filename):
    return "gallery/{}/{}".format(instance.gallery,filename)


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery)
    description = models.CharField(max_length=50)
    img = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description


@receiver(pre_save,sender=Gallery)
def gallery_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)
