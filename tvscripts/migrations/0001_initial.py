# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-07 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scripts', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('epi_number', models.IntegerField()),
                ('season', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('show_name', models.CharField(max_length=500)),
                ('footnote', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Script_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='script',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tvscripts.Script_Tag'),
        ),
    ]