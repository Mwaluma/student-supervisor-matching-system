from django import forms
from django.contrib.auth.models import User
from .models import Lecturer, LecturerProfilePicture
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    #password= forms.CharField(widget= forms.PasswordInput())
    #confirm_password= forms.CharField(widget= forms.PasswordInput())
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model= User
        fields= ['first_name', 'last_name', 'email', 'password1', 'password2']

class LecturerForm(forms.ModelForm):
    class Meta:
        model= Lecturer
        fields= ['phone_number', 'office_address']

class LecturerProfilePictureForm(forms.ModelForm):
    class Meta:
        model= LecturerProfilePicture
        fields= ['picture']

class UserDetailForm(forms.ModelForm):
    class Meta:
        model= User
        fields= ['first_name', 'last_name', 'email']




########################################################################

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']

############################################################################
