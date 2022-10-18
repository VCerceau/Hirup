from django.db import models
import uuid
from .categorie import *

class Competences(models.Model):
    uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, null=True, on_delete = models.SET_NULL)