from django import forms
from User.models.user import User
import uuid

from django import forms

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['profilpic', 'first_name', 'last_name', 'adresse']