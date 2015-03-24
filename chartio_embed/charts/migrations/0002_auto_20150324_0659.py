# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chart',
            options={},
        ),
        migrations.AlterField(
            model_name='chart',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
