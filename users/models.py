from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    fullname = models.CharField(max_length=128, blank=True)


# class Photo(models.Model):
#     image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=150)