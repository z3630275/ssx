# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-01 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('parea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo')),
            ],
        ),
    ]
