from django.db import models
from django.utils import timezone
from datetime import timedelta
from shortuuid.django_fields import ShortUUIDField

from userAuths.models import CustomUser

from django.utils import timezone
import time


class Category(models.Model):
    cid = ShortUUIDField(max_length=40, unique=True, prefix='category/', alphabet='ASCdfghijkl167239')
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'   

    def __str__(self):
        return self.title

class Book(models.Model):
    bid = ShortUUIDField(max_length=40, unique=True, prefix='book/', alphabet='ASCdfghijkl167239')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    favourites = models.ManyToManyField(CustomUser, related_name='favorites', blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes', blank=True)
    readers = models.ManyToManyField(CustomUser, related_name='readers', blank=True)
    pdf_file = models.FileField(max_length=100, upload_to='books')
    cover_image = models.ImageField(max_length=100, upload_to='books/cover')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

class Progress(models.Model):
    pid = ShortUUIDField(max_length=40, unique=True, prefix='progress/', alphabet='ASCdfghijkl167239')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    is_reading = models.BooleanField(default=False, null=True)
    is_complete = models.BooleanField(default=False)

    def set_finish_date(self):
        self.finish_date = self.start_date + timedelta(minutes=2)  
        self.save()

    @property
    def days_remaining(self):
        if self.finish_date:
            remaining = self.finish_date - timezone.now()
            return int(remaining.total_seconds() / 60)
        return None

    
    def mark_as_complete(self):
        self.is_complete = True
        self.finish_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = 'Progresses'

    def __str__(self):
        return self.book.title

class Review(models.Model):
    rid = ShortUUIDField(max_length=40, unique=True, prefix='review/', alphabet='ASCdfghijkl167239')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL,  null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.comment[:10]
