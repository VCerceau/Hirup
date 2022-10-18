from django.db import models
from .presentation import *


class Cv(Presentation):
    name = models.CharField(max_length=30)