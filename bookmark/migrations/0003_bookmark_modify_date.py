# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date'),
        ),
    ]
