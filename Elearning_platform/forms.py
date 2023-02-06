from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User_inherit


class CreateUser(UserCreationForm):
    class Meta:
        model = User_inherit
        fields = ['email', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = User_inherit
        fields = ['email', 'first_name', 'last_name', 'phone', 'bio', 'image', ]
