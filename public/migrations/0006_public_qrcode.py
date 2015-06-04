# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_public_addtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='qrcode',
            field=models.TextField(null=True),
        ),
    ]
