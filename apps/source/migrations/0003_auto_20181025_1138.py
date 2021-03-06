# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-25 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_auto_20181025_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bind_host',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bind_host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.BindHost'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='host_group',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='host_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source.HostGroup'),
        ),
    ]
