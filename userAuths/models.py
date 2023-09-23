from django.db import models
from django.contrib.auth.models import AbstractUser

CAREER = (
    ('teacher', 'Teacher'),
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('designer', 'Software Designer'),
    ('developer', 'Software Developer'),
)

LOCATION = (
    ('kenya', 'Nairobi, Kenya'),
    ('uganda', 'Kampala, Uganda'),
    ('nigeria', 'Lagos, Nigeria'),
    ('egypt', 'Cairo, Egypt'),
    ('Eritrea', 'Asmara, Eritrea'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200)
    profile_pic = models.ImageField(default='profile.png', upload_to='profile', null=True, blank=True)
    career = models.CharField(null=True, blank=True, choices=CAREER, max_length=100)
    loacation = models.CharField(null=True, blank=True, choices=LOCATION, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
