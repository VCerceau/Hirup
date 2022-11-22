from django.db import models
from .presentation import *
from User.models.personne import *
from .introduction import *


class Cv(Presentation):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(Personne, on_delete=models.CASCADE)
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    ord_xp = models.IntegerField(null=True)
    ord_form = models.IntegerField(null=True)
    ord_comp = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.name}, {self.user}"