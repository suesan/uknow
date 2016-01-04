# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=30, unique=True, verbose_name='username'),
        ),
    ]