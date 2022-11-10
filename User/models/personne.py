from django.db import models
from .user import *


class Personne(User):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    
    ROLE_CHOICES = [
        ('STUDENT', 'Eleve'),
        ('TEACHER', 'Professeur'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )