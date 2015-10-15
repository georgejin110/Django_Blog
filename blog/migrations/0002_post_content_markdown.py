# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_markdown',
            field=models.TextField(help_text=b'Using markdown syntax', verbose_name=b'Markdown', blank=True),
        ),
    ]
