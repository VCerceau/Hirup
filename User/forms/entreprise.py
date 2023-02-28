from django.db import models

from User.models.entreprise import Entreprise
from .user import *

from django import forms


class EntrepriseSignup(forms.ModelForm):
    username = forms.EmailField(widget=forms.EmailInput, label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Entreprise
        fields = ['name', 'siret', 'username', 'password']