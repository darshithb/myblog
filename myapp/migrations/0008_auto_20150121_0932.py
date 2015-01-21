# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Address',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Date_birth',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Phone_number',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
