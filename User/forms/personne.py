from django.db import models
from User.models.personne import *

from django import forms

class EditProfileForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'email',
        'value': '{{personne.mail}}',
        'readonly': True,
    }))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'prenom',
        'value': '{{personne.firstname}}',
        'readonly': True,
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'prenom',
        'value': '{{personne.lastname}}',
        'readonly': True,
    }))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'telephone',
        'pattern': '[0-9]{2}{5}',
        'value': '{{personne.phonenumber}}',
        'readonly': True,
    }))
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'adresse',
        'value': '{{personne.adress}}',
        'readonly': True,
    }))
    profilpic = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'id': 'pp',
        'class': 'img-fluid rounded-circle',
    }))
    
    def save(self, personne):
        personne.email = self.cleaned_data['email']
        personne.firstname = self.cleaned_data['firstname']
        personne.lastname = self.cleaned_data['lastname']
        personne.phonenumber = self.cleaned_data['phonenumber']
        personne.adress = self.cleaned_data['adress']
        personne.profilpic = self.cleaned_data['profilpic']
        personne.save()
        return personne