from django.db import models
import uuid
from .categorie import *
from .cv import *
from User.models import Personne


class Formation(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title = models.CharField(max_length=32)
    description = models.TextField()
    order = models.IntegerField()
    mention = models.TextField()
    categorie = models.ForeignKey(Categorie, null=True, on_delete = models.SET_NULL)
    certifie = models.ForeignKey(Personne, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)

