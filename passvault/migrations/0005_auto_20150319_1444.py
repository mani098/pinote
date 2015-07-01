# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passvault', '0004_auto_20150319_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passvault',
            old_name='custom_fiels',
            new_name='custom_fields',
        ),
    ]
