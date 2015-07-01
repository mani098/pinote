# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblinks', '0004_auto_20150314_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblinks',
            name='category',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weblinks',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='weblinks',
            name='url',
            field=models.URLField(),
        ),
    ]
