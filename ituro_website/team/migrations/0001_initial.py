# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to=team.models.get_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mission', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]
