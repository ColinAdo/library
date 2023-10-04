from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Book, Progress, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'display_cover_image', 'pdf_file', 'short_description']

    def display_cover_image(self, obj):
        return format_html('<img src="{}" style="border-radius: 5px; width="50" height="50" />', obj.cover_image.url)

    def short_description(self, obj):
        words = obj.description.split()

        short_desc = ' '.join(words[:10])
        if len(words) > 10:
            short_desc += '...'
        return short_desc
    short_description.short_description = 'description'


class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'start_date', 'finish_date','is_reading' , 'is_complete']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'date', 'comment']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Review, ReviewAdmin)
