# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-06 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170506_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.PostFeaturedImage'),
        ),
    ]
