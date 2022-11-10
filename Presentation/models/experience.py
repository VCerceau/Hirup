from django.db import models
import uuid
from .categorie import *
from User.models import Personne


class Experience(models.Model):
     uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
     title = models.TextField()
     description = models.TextField()
     categorie = models.ForeignKey(Categorie, null=True, on_delete = models.SET_NULL)
     certifie = models.ForeignKey(Personne, on_delete=models.CASCADE)
