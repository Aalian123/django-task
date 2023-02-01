from django.contrib import admin
from .models import User_inherit, Teacher, Course, Student


# Register your models here.

# Re-arranging user model fields
class Signup_variables(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        ('User Info', {
            'fields': ('first_name', 'last_name', 'email', 'password',)
        }),
        ('User Status', {
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Groups and Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
    )


# Re-arranging Teacher model Fields
class TeacherForm(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'speciality']
    list_filter = ('first_name', 'speciality')
    search_fields = ('first_name', 'speciality')
    fieldsets = (
        ('Teacher Info', {
            'fields': ('first_name', 'last_name', 'email', 'password',)
        }),
        ('Teacher Speciality', {
            'fields': ('speciality',)
        }),

    )


# Re-arranging Student model fields
class StudentForm(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    fieldsets = (
        ('Student Info', {
            'fields': ('first_name', 'last_name', 'email', 'password', 'course',)
        }),

    )


class CourseForm(admin.ModelAdmin):
    list_display = ['course_name', 'course_category', 'teacher_name']


# admin.site.register(User_info, Signup_variables)
admin.site.register(User_inherit, Signup_variables)
admin.site.register(Teacher, TeacherForm)
admin.site.register(Course, CourseForm)
admin.site.register(Student, StudentForm)

