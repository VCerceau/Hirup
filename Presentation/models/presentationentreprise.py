from django.db import models
from .presentation import *
from User.models.entreprise import *


class PresentationEntreprise(Presentation):
    description = models.TextField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)