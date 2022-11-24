from django.db import models
from django import forms
from .user import *
from User.models import *


from django import forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
