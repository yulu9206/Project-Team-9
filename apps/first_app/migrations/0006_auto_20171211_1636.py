# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-11 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20171210_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
