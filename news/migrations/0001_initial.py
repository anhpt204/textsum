# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_import', models.DateTimeField(verbose_name=b'Ng\xc3\xa0y import d\xe1\xbb\xaf li\xe1\xbb\x87u')),
                ('dir_path', models.FilePathField(allow_files=False, verbose_name=b'Th\xc6\xb0 m\xe1\xbb\xa5c d\xe1\xbb\xaf li\xe1\xbb\x87u', allow_folders=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsSum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name=b'URL')),
                ('domain', models.CharField(max_length=50, verbose_name=b'Domain')),
                ('summary', models.TextField(verbose_name=b'T\xc3\xb3m t\xe1\xba\xaft')),
            ],
        ),
        migrations.CreateModel(
            name='TopicSum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='newssum',
            name='in_topic',
            field=models.ForeignKey(verbose_name=b'Thu\xe1\xbb\x99c ch\xe1\xbb\xa7 \xc4\x91\xe1\xbb\x81', to='news.TopicSum'),
        ),
    ]
