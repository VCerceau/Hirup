from django.db import models
from django import form
from models.user import User
import uuid

from django import forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User