# forms.py
from django import forms

class CVSearchForm(forms.Form):
    query = forms.CharField(label='Rechercher un CV', max_length=100)
