from django.db import models
from .presentation import *
from User.models.personne import *


class Cv(Presentation):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(Personne, on_delete=models.CASCADE)
    introduction = models.TextField()
    ord_xp = models.IntegerField(null=True, default=1)
    ord_form = models.IntegerField(null=True, default=2)
    ord_comp = models.IntegerField(null=True, default=3)
    
    def __str__(self):
        return f"{self.name}, {self.user}"