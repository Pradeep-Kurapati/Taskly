from django.forms import ModelForm
# from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Task, Profile


# Register a User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User login 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create Task
class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content',]
        # exclude = ['user',]


# Ptofile Management
class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email',]


# Update a Profile Picture
class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ['profile_pic',]
        

