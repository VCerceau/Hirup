from django.db import models
from django import forms
import os
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    username = models.EmailField(('email'),unique=True, max_length=128)
    password = models.CharField(max_length=256)
    adresse = models.CharField(blank=True, null=True, max_length=128)
    profilpic = models.ImageField(default='default.png', upload_to='user/pp', blank=True, null=True)
    
    __original_pass = None
    def __str__(self):
        return f"{self.username}"
    
    def __init__(self, *args, **kwargs):
        self.my_field_supplied = 'my_field' in kwargs # True if my_field provided explicitly, false otherwise
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
    
    def save(self,*args, **kwargs):
        file_name, file_extension = os.path.splitext(self.profilpic.name)
        if self.my_field_supplied:
            self.profilpic.name = str(self.uuid) + file_extension
        if self.password != self.__original_pass and self.is_staff == 0 :
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
            self.__original_pass = self.password           
        else:
            super().save(*args, **kwargs)
    @property
    def get_photo_url(self):
        return self.profilpic