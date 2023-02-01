from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class UserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        import pdb
        pdb.set_trace()
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# custom model but subclassed by AbstractUser class
class User_inherit(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField("first name", max_length=150, blank=True, null=True, default=None)
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

