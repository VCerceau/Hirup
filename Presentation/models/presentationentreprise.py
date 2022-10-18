from django.db import models
from .presentation import *


class PresentationEntreprise(Presentation):
    description = models.CharField(max_length=255)