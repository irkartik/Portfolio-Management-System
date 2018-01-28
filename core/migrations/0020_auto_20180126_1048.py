# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180126_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misctext',
            name='profilepic_url',
            field=models.FileField(upload_to='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='misctext',
            name='resume_url',
            field=models.FileField(upload_to='', max_length=1000),
        ),
    ]
