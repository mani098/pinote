# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passvault', '0002_auto_20150314_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='passvault',
            name='category',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='passvault',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
