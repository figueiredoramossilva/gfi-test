# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-31 02:10
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import treewidget.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Configurator', '0003_customer_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='equipment',
            field=treewidget.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Configurator.Equipment'),
        ),
    ]