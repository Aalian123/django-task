from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_info, User_inherit


# Register your models here.
class Signup_variables(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


admin.site.register(User_info, Signup_variables)
admin.site.register(User_inherit)
