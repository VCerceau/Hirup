from django.db import models
from .user import *

from django import forms
class PersonneForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User