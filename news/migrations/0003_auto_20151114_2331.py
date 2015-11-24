# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151114_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicsum',
            name='date_published',
            field=models.DateField(null=True, verbose_name=b'date published'),
        ),
    ]
