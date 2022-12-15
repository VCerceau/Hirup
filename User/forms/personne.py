from django.db import models
from User.models.personne import *

from django import forms

class EditProfileForm(forms.Form):
    profilpic = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'id': 'pp',
        'class': 'img-fluid rounded-circle',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'email',
        'value': '{{user.personne.mail}}',
    }))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'firstname',
        'value': '{{user.personne.firstname}}',
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'lastname',
        'value': '{{user.personne.lastname}}',
    }))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'phonenumber',
        'pattern': '[0-9]{2}{5}',
        'value': '{{user.personne.phonenumber}}',
    }))
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0',
        'id': 'adress',
        'value': '{{user.personne.adress}}',
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