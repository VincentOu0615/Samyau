# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170511_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='EnShortName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Fax',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='PoName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Web',
            field=models.URLField(null=True),
        ),
    ]
