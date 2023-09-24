from django.db import models
from django.utils import timezone
from datetime import timedelta
from shortuuid.django_fields import ShortUUIDField

from userAuths.models import CustomUser


class Category(models.Model):
    cid = ShortUUIDField(max_length=30, unique=True, prefix='category=?', alphabet='ASCdfghijkl167239')
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'   

    def __str__(self):
        return self.title

class Book(models.Model):
    bid = ShortUUIDField(max_length=30, unique=True, prefix='book=?', alphabet='ASCdfghijkl167239')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf_file = models.FileField(max_length=100, upload_to='books')
    cover_image = models.ImageField(max_length=100, upload_to='books/cover')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

class Progress(models.Model):
    pid = ShortUUIDField(max_length=30, unique=True, prefix='progress=?', alphabet='ASCdfghijkl167239')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def mark_as_complete(self):
        self.is_complete = True
        self.finish_date = timezone.now()
        self.save()

    def set_finish_date(self):
        self.finish_date = self.start_date + timedelta(days=7)
        self.save()

    class Meta:
        verbose_name_plural = 'Progresses'

    def __str__(self):
        return self.is_complete

class Review(models.Model):
    rid = ShortUUIDField(max_length=30, unique=True, prefix='review=?', alphabet='ASCdfghijkl167239')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.comment[:10]
