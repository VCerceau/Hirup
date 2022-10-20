from django.db import models
import uuid


class Categorie(models.Model):
     uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
     name = models.TextField()