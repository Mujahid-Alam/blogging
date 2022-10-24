from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'title', 'description', 'url', 'image_tag', 'add_date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('cat',)
    list_per_page: 2

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js', 'js/script.js',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)