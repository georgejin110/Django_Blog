from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'author', 'content')
            }),
        ('Date',{
            'fields': ('created_date', 'published_date')
            })
        )

admin.site.register(Post, PostAdmin)