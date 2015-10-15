#!-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager

@python_2_unicode_compatible
class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Programming', (
            ('python', 'Python'),
            ('ruby', 'Ruby'),
            )
        ),
        ('Music', (
            ('pop', 'Pop'),

            )
        ),
        ('unknown', 'Unknown'),
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(help_text="Generating a short url..", blank=True)
    content_markdown = models.TextField('Markdown Editor', help_text='Using markdown syntax', blank=True)
    content = models.TextField(default="Writing something you want...", blank=True)
    last_modified = models.DateTimeField('last modified', auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='nuknown')

    class Meta:
        ordering = ["-published_date"]

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'pk': self.pk})

    def __str__(self):
        return self.title

    def save(self):
        import markdown2
        self.content_markdown = markdown2.markdown(self.content_markdown)
        super(Post, self).save()

        

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
