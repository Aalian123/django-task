from .models import User_inherit
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Inherited_form(forms.ModelForm):
    class Meta:
        model = User_inherit
        fields = ['email', 'first_name', 'last_name', 'email']


class CreateUser(UserCreationForm):
    class Meta:
        model = User_inherit
        fields = ['email', 'first_name', 'last_name', 'email']
