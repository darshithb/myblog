# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150121_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Date_birth',
            new_name='date_birth',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
