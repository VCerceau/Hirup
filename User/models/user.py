from django.db import models
from django import forms
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    street = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    code = models.IntegerField(null=True)
    country = models.CharField(max_length=64, null=True)
    profilpic = models.CharField(default='default.png', max_length=512)
    
    
    def __str__(self):
        return f"{self.email}"
    
    def save(self,*args, **kwargs):
        self.password = make_password(self.password, salt=None)
        super().save(*args, **kwargs)
        
    @property
    def get_photo_url(self):
        return 'img/user/ProfilPic/%s' % self.profilpic