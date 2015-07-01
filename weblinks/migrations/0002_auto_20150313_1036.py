# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weblinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblinks',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weblinks',
            name='url',
            field=models.URLField(max_length=700),
        ),
    ]
