from django.db import models
from .user import *
from User.models import User


class AdminForm(User):
    model = User
    fields = ['email','password','name','street','city','code','country']
