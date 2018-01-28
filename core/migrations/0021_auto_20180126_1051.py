# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20180126_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='misctext',
            old_name='profilepic_url',
            new_name='profilepic',
        ),
        migrations.RenameField(
            model_name='misctext',
            old_name='resume_url',
            new_name='resume',
        ),
    ]
