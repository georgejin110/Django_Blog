from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    fieldsets = (
        ('Post Information', {'fields': [('title', 'category'), 'slug', 'author', 'content_markdown', 'tags']}),
    )
    list_display = ['title', 'category', 'author']

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'body', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)