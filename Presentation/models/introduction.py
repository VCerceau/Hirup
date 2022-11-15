from django.db import models
import uuid
from .categorie import *
from User.models.user import *

class Introduction(models.Model):
    uuid = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    description = models.TextField()