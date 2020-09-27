from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_display_links = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ['title']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ['title', 'slug']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
