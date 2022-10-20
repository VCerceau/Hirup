from django.db import models
from .presentation import *


class Cv(Presentation):
    name = models.TextField()
    eleves = models.ForeignKey('User.Personnes', on_delete=models.CASCADE)