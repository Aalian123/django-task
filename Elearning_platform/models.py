from django.db import models
from django.contrib.auth.models import AbstractUser


# custom model but subclassed by AbstractUser class
class User_inherit(AbstractUser):
    bio = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'user_info'
