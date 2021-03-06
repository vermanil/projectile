# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 04:13
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20161119_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ' Select Skills'), ('python', 'Python'), ('django', 'Django'), ('java', 'Java'), ('html', 'HTML'), ('css', 'CSS'), ('javascript', 'JavaScript'), ('bootstrap', 'Bootstrap'), ('php', 'PHP'), ('mySql', 'MySql')], max_length=6000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ' Select Skills'), ('Python', 'Python'), ('Django', 'Django'), ('Java', 'Java'), ('html', 'HTML'), ('css', 'CSS'), ('javascript', 'JavaScript'), ('bootstrap', 'Bootstrap'), ('php', 'PHP'), ('mySql', 'MySql')], max_length=6000),
        ),
    ]
