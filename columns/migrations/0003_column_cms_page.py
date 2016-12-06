# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-06 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('columns', '0002_auto_20161020_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='cms_page',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page'),
        ),
    ]
