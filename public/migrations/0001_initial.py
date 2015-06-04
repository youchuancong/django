# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='public',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('num', models.CharField(unique=True, max_length=128)),
                ('isattention', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64, null=True)),
                ('url', models.CharField(max_length=256)),
                ('qq', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='webchat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('isuse', models.BooleanField(default=False)),
                ('isblock', models.BooleanField(default=False)),
            ],
        ),
    ]
