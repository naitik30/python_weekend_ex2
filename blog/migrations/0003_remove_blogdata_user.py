# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 01:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogdata_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdata',
            name='user',
        ),
    ]
