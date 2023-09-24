from django.contrib import admin
from .models import Category, Book, Progress, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'cover_image']

class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'start_date', 'finish_date', 'is_complete']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'date', 'comment']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Review, ReviewAdmin)
