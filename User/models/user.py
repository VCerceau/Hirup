from django.db import models
import time
import os
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField



class User(AbstractUser):
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    username = models.EmailField(('email'),unique=True, max_length=128)
    password = models.CharField(max_length=256)
    adresse = models.CharField(blank=True, null=True, max_length=128)
    profilpic = ResizedImageField(size=[200,200], default='user/pp/default.webp', upload_to='user/pp', null= True)
    
    __original_pass = None
    __original_image = None
    
    def __str__(self):
        return f"{self.username, self.uuid}"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
        self.__original_image = self.profilpic.name
    
    def save(self,*args, **kwargs):
        # if os.path.isfile(self.get_photo_full_path()):
        #     os.remove(self.get_photo_full_path())
        file_name, file_extension = os.path.splitext(self.profilpic.name)
        if self.profilpic.name != "user/pp/default.webp" and self.profilpic.name != self.__original_image:
            self.profilpic.name = str(self.uuid)+ '-' + str(int(time.time())) +  file_extension
        self.__original_image = self.profilpic.name

        if self.password != self.__original_pass and (self.is_staff == 0 or issubclass()) :
            self.password = make_password(self.password)
            super().save(*args, **kwargs)
            self.__original_pass = self.password           
        else:
            super().save(*args, **kwargs)
        for filenames in os.listdir('Media/user/pp'):
            if str(self.uuid) in filenames and ('user/pp/' + filenames) != self.profilpic.name:
                os.remove('Media/user/pp/'+ filenames)
    @property
    def get_photo_url(self):
        return self.profilpic
    
    def get_photo_full_path(self):
        return ('/Media/') + str(self.profilpic)