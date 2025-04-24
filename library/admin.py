from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_available')
    list_filter = ('is_available', 'author', 'published_date')
    search_fields = ('title', 'author__name', 'description')
    date_hierarchy = 'published_date'
    ordering = ('-created_at',)
