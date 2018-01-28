# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20180126_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic',
            name='marksheet',
        ),
        migrations.AlterField(
            model_name='academic',
            name='degree',
            field=models.FileField(null=True, max_length=1000, blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='certificate',
            field=models.FileField(null=True, max_length=10000, verbose_name='Certificate Upload', upload_to='', blank=True),
        ),
    ]
