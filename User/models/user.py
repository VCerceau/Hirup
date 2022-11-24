from django.db import models
from django import forms
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    adresse = models.CharField(null=True, max_length=128)
    profilpic = models.ImageField(default='user/pp/default.png', upload_to='user/pp', null=True)
    
    __original_pass = None
    def __str__(self):
        return f"{self.email}"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
    
    def save(self,*args, **kwargs):
        if not self.pk or self.password != self.__original_pass:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
            self.__original_pass = self.password
        
    @property
    def get_photo_url(self):
        return 'img/user/ProfilPic/%s' % self.profilpic