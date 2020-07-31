from django.contrib import admin
from .models import Post, Category


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
