# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20150513_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='webchat',
            name='updatetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='public',
            name='desc',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='public',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='public',
            name='qq',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
