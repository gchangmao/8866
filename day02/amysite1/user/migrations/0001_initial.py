# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-28 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11, verbose_name='用户名')),
                ('password', models.CharField(max_length=11, verbose_name='密码')),
                ('nickname', models.CharField(max_length=11, verbose_name='昵称')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
