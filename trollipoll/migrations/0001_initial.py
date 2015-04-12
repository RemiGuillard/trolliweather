# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('city_name', models.CharField(max_length=64)),
                ('country_name', models.CharField(max_length=64)),
                ('time_interval', models.IntegerField(default=24)),
                ('api_location', models.CharField(max_length=200)),
            ],
        ),
    ]
