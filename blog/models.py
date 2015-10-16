#!/usr/bin/env python
#!-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager
from django.db.models import permalink
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(help_text="Generating a short url..", blank=True)
    # content_markdown = models.TextField('Markdown Editor', help_text='Using markdown syntax', blank=True)
    content = models.TextField(blank=True)
    last_modified = models.DateTimeField('last modified', auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    category = models.ForeignKey('blog.Category')

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    # @permalink
    def get_absolute_url(self):
        return reverse('blog.views.post', kwargs={'slug': self.slug})

@python_2_unicode_compatible
class Category(models.Model):  
    title = models.CharField('Category', max_length=30, default='Unknown')
    slug = models.SlugField(max_length=30, blank=True)

    def __str__(self):
        return self.title

    # @permalink
    def get_absolute_url(self):
        return reverse('blog.views.category', kwargs={'slug': self.slug})    

@python_2_unicode_compatible
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=40, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return ("%s: %s" % (self.post, self.body[:60]))
