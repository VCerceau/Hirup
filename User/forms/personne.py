from django.db import models
from User.models.__init__ import Personne, User

from django import forms

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['profilpic', 'first_name', 'last_name', 'adresse']

class EditProfileForm(forms.ModelForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control no-bg'}),)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control no-bg'}), required=False)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control no-bg'}), required=False)
    adresse = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control no-bg'}), required=False)
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control no-bg'}), required=False)
    class Meta:
        model = Personne
        fields = ['username', 'firstname', 'lastname', 'adresse', 'phonenumber']