# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blogpost_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='comments',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
    ]
