from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


# custom model but subclassed by AbstractUser class
class User_inherit(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField("first name", max_length=150, blank=True, null=True, default=None)
    last_name = models.CharField("last name", max_length=150, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.TextField(blank=True)
    bio = models.TextField(max_length=255, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        if self.first_name is None:
            self.first_name = self.last_name

        self.email = self.__class__.objects.normalize_email(self.email)

    class Meta:
        verbose_name_plural = 'user_info'


# Course model
class Teacher(User_inherit):
    teacher_id = models.BigAutoField(primary_key=True)
    speciality = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Teacher'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Course model
class Course(models.Model):
    COURSE_CATEGORY_CHOICES = [('Technology', 'Technology'),
                               ('History', 'History'),
                               ('Biology', 'Biology')
                               ]
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_category = models.CharField(max_length=30, choices=COURSE_CATEGORY_CHOICES, default='Technology')
    teacher_name = models.ForeignKey(Teacher, to_field="teacher_id", max_length=200, on_delete=models.CASCADE)
    upload_course = models.FileField(upload_to='media', null=True)
    duration = models.TextField(max_length=20)

    class Meta:
        verbose_name_plural = 'Course'

    def __str__(self):
        return f"{self.course_name}--{self.teacher_name}"


# student model
class Student(User_inherit):
    student_id = models.BigAutoField(primary_key=True)
    course = models.ManyToManyField(Course, max_length=200)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# cron job model
class CronJob(models.Model):
    name = models.CharField(max_length=255, null=True)
    time = models.DateTimeField()
