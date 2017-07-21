# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-21 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_remove_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalogue.Category'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
