# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20161029_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectskills',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Project'),
        ),
    ]