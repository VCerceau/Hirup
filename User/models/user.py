from django.db import models
from django import forms
import uuid

class User(models.Model):
     uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
     email = models.EmailField()
     password = models.TextField(max_length=64)
     street = models.TextField()
     city = models.TextField()
     code = models.TextField()
     country = models.TextField()
     

     class Meta:
        abstract = True

