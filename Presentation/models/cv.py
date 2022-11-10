from django.db import models
from .presentation import *


class Cv(Presentation):
    name = models.TextField()
    eleves = models.ForeignKey('User.Personne', on_delete=models.CASCADE)