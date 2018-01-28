# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20180126_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='certificate',
            field=models.FileField(upload_to='', verbose_name='Certificate Upload', max_length=10000),
        ),
    ]
