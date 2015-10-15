# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default=b'a short url', help_text=b'Generating a short url..')),
                ('content', models.TextField(default=b'Writing something you want...', blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name=b'last modified')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default=b'nuknown', max_length=30, choices=[(b'Programming', ((b'python', b'Python'), (b'ruby', b'Ruby'))), (b'Music', ((b'pop', b'Pop'),)), (b'unknown', b'Unknown')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
