from .models import User_info
from django import forms


# Creating model form of User_info model
class UserForm(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = User_info
        # It includes all the fields of model
        fields = '__all__'
