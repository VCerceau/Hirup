from django.db import models
from .user import User


class Admin(User):
    is_staff = 1
    is_superuser = 1    
    
    class Meta:
        verbose_name = 'Admin'
    