# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-25 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_auto_20181025_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostgroup',
            name='bind_hosts',
        ),
        migrations.AddField(
            model_name='bindhost',
            name='host_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.HostGroup'),
        ),
    ]