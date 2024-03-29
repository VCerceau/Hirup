from django.db import models
import time
import os
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.utils.text import slugify




class User(AbstractUser):
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    username = models.EmailField(('email'),unique=True, max_length=128)
    password = models.CharField(max_length=256)
    adresse = models.CharField(blank=True, null=True, max_length=128)
    profilpic = ResizedImageField(size=[200,200], crop=['middle', 'center'], default='user/pp/default.webp', upload_to='user/pp/', null = True)
    phonenumber = models.CharField(('numéro de téléphone'),max_length=50, null=True, blank=True)
    
    __original_pass = None
    __original_image = None
    __original_slug = None
    
    def __str__(self):
        return f"{self.username, self.uuid}"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
        self.__original_image = self.profilpic.name
    
    def save(self,*args, **kwargs):

        # file_name, file_extension = os.path.splitext(self.profilpic.name)
        # if self.profilpic.name != "user/pp/default.webp" and self.profilpic.name != self.__original_image:
        #     self.profilpic.name = str(self.uuid)+ '-' + str(int(time.time())) +  file_extension
        # self.__original_image = self.profilpic.name
        super().save(*args, **kwargs)
        # for filenames in os.listdir('Media/user/pp'):
        #     if str(self.uuid) in filenames and ('user/pp/' + filenames) != self.profilpic.name:
        #         os.remove('Media/user/pp/'+ filenames)
    @property
    def get_photo_url(self):
        return self.profilpic
    
    def get_photo_full_path(self):
        return ('/Media/') + str(self.profilpic)
    
    def mail(self):
        return self.username