from django.db import models
from django import forms
from .user import *
from User.models import *


class AdminForm(forms.Form):
    class Meta:    
        model = Admin
        fields = ['uuid','email','password','name','street','city','code','country']
