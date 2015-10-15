# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content_markdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_markdown',
            field=models.TextField(help_text=b'Using markdown syntax', verbose_name=b'Markdown Editor', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text=b'Generating a short url..', blank=True),
        ),
    ]
