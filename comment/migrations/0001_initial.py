# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 14:05
from __future__ import unicode_literals

import blog.models
import collect.models
from django.db import migrations, models
import faquestion.models
import usercenter.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_type', models.CharField(choices=[('user', usercenter.models.User), ('blog', blog.models.BlogPost), ('collect', collect.models.Collect), ('question', faquestion.models.FAQuestion)], default='blog', max_length=10, verbose_name='评论对象')),
                ('obj_id', models.IntegerField(null=True, verbose_name='评论对象ID')),
                ('reply_content', models.TextField(verbose_name='评论内容')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('is_active', models.CharField(choices=[('deleted', '已删除'), ('active', '正常')], default='active', max_length=10, verbose_name='评论状态')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
