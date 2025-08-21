from django.contrib import admin
from apps.blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "cat")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "cat")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
