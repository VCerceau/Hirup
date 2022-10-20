from django.db import models
from .user import *


class Personnes(User):
    firstname = models.TextField()
    lastname = models.TextField()
    role = models.TextField()