# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblinks', '0003_auto_20150313_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblinks',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
