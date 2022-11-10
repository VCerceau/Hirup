from django.db import models
from django import forms
import uuid

class User(models.Model):
     uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
     email = models.EmailField()
     password = models.CharField(max_length=64)
     street = models.CharField(max_length=64)
     city = models.CharField(max_length=64)
     code = models.IntegerField()
     country = models.CharField(max_length=64)
     

     class Meta: 
        abstract = True

