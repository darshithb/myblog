# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2014, 11, 21, 9, 35, 55, 55488, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
    ]
