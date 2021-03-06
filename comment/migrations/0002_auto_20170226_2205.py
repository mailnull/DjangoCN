# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='我的评论'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented', to=settings.AUTH_USER_MODEL, verbose_name='被评论人'),
        ),
    ]
