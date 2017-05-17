# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 16:05
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(allow_unicode=True, max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]