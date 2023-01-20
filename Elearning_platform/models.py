from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom model for users data
class User_info(models.Model):
    user_id = models.IntegerField(default=0, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField(max_length=13)
    test = models.CharField(max_length=12)

    # Method to get all data of model from Database
    @staticmethod
    def get_all_users():
        return User_info.objects.all()


# Also custom model but subclassed by AbstractUser class
class User_inherit(AbstractUser):
    bio = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'user_info'

    # method to get all users
    @staticmethod
    def get_all_users():
        return User_info.objects.all()
