# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-07 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170506_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfeaturedimage',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/%Y/%m/%d', width_field='width_field'),
        ),
    ]
