from django.db import models
from .user import *


class Admin(User):
    name = models.TextField()
