# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170909_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brief',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
