# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20180126_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic',
            name='certificate',
            field=models.FileField(upload_to='', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='degree',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
