# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180126_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
