from django.db import models
from .user import *


class Personne(User):
    pass
    
    class Meta:
        verbose_name = 'Personne'