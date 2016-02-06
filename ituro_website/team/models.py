from __future__ import unicode_literals
from django.db import models


def get_upload_path(instance,filename):
    return "team/{}/{}".format(instance.name,filename)


class Team(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team)
    full_name = models.CharField(max_length=100)
    mission = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.full_name
