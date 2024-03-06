from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ["user",]


class RequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        exclude = ["owner",]
