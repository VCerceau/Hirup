from django import forms
from django.forms import ClearableFileInput
from User.models.user import User
from User.models.personne import Personne
import uuid
from django.core.validators import RegexValidator


from django import forms

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['profilpic', 'first_name', 'last_name', 'adresse']



class ProfileForm(forms.ModelForm):
    username = forms.EmailField(label="Email")
    adresse = forms.CharField(max_length=200, required=False)
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]{7,15}$',
        message="Le numéro doit être du format: '+999999999'. Exemple:'+33612345678' Jusqu'à 15 chiffres."
    )
    phonenumber = forms.CharField(validators=[phone_regex], required=False)
    profilpic = forms.ImageField(label="")
    class Meta:
      model = User
      fields = ['profilpic', 'adresse', 'phonenumber', 'username']
