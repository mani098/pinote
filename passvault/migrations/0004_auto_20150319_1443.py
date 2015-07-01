# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('passvault', '0003_auto_20150318_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passvault',
            name='url',
        ),
        migrations.RemoveField(
            model_name='passvault',
            name='username',
        ),
        migrations.AddField(
            model_name='passvault',
            name='custom_fiels',
            field=jsonfield.fields.JSONCharField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
