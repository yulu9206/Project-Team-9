# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20171204_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='userX', max_length=38),
        ),
    ]