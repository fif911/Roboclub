# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-10 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20161208_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='f_report',
            name='nameOfDocument1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]