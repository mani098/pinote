# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblinks', '0002_auto_20150313_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblinks',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
