# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicsum',
            name='date_import',
            field=models.DateField(default=datetime.datetime(2015, 11, 14, 23, 29, 33, 348321, tzinfo=utc), verbose_name=b'date imported'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topicsum',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2015, 11, 14, 23, 29, 47, 118035, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='importlog',
            name='date_import',
            field=models.DateField(verbose_name=b'Ng\xc3\xa0y import d\xe1\xbb\xaf li\xe1\xbb\x87u'),
        ),
        migrations.AlterField(
            model_name='importlog',
            name='dir_path',
            field=models.CharField(default=b'/home/pta/git/textsum/models/', max_length=50, verbose_name=b'Th\xc6\xb0 m\xe1\xbb\xa5c d\xe1\xbb\xaf li\xe1\xbb\x87u'),
        ),
    ]
