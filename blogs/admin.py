from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'id')


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)