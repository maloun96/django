# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-03 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20161228_0509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcategory_id',
            new_name='subcategory',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_id',
            new_name='category',
        ),
    ]
