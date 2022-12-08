from django.db import models
from .user import *


class Personne(User):
    firstname = models.CharField(max_length=64, null=True, blank=True)
    lastname = models.CharField(max_length=64, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Personne'