# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_analytics', '0002_auto_20150224_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherPrediction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherSource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('source_uri', models.URLField()),
                ('poll_frequency', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='weatherprediction',
            name='source',
            field=models.ForeignKey(to='weather_analytics.WeatherSource'),
        ),
    ]
