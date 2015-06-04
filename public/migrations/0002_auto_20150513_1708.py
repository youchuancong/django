# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hellomsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=128)),
                ('isactive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='resmsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=256)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='public',
            name='id',
        ),
        migrations.RemoveField(
            model_name='webchat',
            name='id',
        ),
        migrations.AddField(
            model_name='public',
            name='ishello',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='public',
            name='num',
            field=models.CharField(max_length=128, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='webchat',
            name='num',
            field=models.CharField(max_length=32, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='resmsg',
            name='num',
            field=models.ForeignKey(to='public.public'),
        ),
    ]
