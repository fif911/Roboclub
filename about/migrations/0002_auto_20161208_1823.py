# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.TextField(max_length=30)),
                ('body', models.TextField()),
                ('document1', models.URLField(blank=True, max_length=150, null=True)),
                ('document2', models.URLField(blank=True, max_length=150, null=True)),
                ('document3', models.URLField(blank=True, max_length=150, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.DeleteModel(
            name='Freports',
        ),
    ]