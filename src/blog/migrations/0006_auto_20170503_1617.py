# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-03 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
