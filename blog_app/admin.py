from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, BlogImage

# Register your models here.
class PostAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'date_created', 'is_published', 'is_private']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(BlogImage)
