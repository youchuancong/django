# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_public_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='webchat',
            name='lastusetime',
            field=models.DateTimeField(null=True),
        ),
    ]
