# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='description',
            new_name='address',
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(null=True, blank=True),
        ),
    ]
