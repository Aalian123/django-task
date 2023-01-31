from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User_inherit, Teacher, Course, Student, StudentCourse, StudentTeacher


# Register your models here.
class Signup_variables(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']


# admin.site.register(User_info, Signup_variables)
admin.site.register(User_inherit,Signup_variables)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentTeacher)
admin.site.register(StudentCourse)
