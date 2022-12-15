from django.db import models
from .user import *


class Entreprise(User):
    name = models.TextField()
    siret = models.IntegerField()

    class Meta:
        verbose_name = 'Entreprise'
        