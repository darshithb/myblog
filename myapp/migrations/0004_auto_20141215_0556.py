# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blog_first_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
            preserve_default=True,
        ),
    ]
