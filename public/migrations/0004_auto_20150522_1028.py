# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20150520_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webchat',
            options={'ordering': ['-updatetime']},
        ),
        migrations.AddField(
            model_name='public',
            name='readcount',
            field=models.IntegerField(null=True),
        ),
    ]
