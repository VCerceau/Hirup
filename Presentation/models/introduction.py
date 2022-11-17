from django.db import models
import uuid
from .categorie import *
from User.models.user import *

class Introduction(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    name = models.CharField(max_length=32)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name}, {self.uuid}"