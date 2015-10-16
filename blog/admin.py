from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    fieldsets = (
        ('Post Information', {'fields': ['title', 'category', 'slug', 'author', 'content', 'tags']}),
    )
    list_display = ['title', 'category', 'author']

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'body', 'post']

# class CategoryAdmin(admin.ModelAdmin):


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)