# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150716_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
