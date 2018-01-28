# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20180122_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_url',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(max_length=10000, upload_to='', default=1),
            preserve_default=False,
        ),
    ]
