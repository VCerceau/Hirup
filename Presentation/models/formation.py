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
    mention = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete = models.SET_NULL)
    certifie = models.ForeignKey(Personne,null=True, on_delete=models.CASCADE)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}, {self.uuid}"