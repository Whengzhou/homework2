# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_auto_20161120_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('dislike', 'dislike'), ('like', 'like')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='belong_to',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]