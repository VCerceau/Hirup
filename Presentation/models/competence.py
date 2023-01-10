from django.db import models
import uuid
from .categorie import *
from .cv import *
from User.models import Personne

class Competence(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title = models.CharField(max_length=64)
    description = models.TextField()
    order = models.IntegerField()
    categorie = models.ForeignKey(Categorie, null=True, on_delete = models.SET_NULL)
    certifie = models.ForeignKey(Personne,null=True, blank=True, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)