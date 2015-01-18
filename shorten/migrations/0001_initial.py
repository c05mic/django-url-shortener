# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('date_last_accessed', models.DateTimeField(null=True)),
                ('visits', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
