from django.db import models
from .user import User


class Admin(User):
    name = models.TextField()
    