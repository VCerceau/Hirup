import itertools
from django.db import models
from .user import *


class Entreprise(User):
    name = models.CharField(max_length=64)
    siret = models.IntegerField()

    class Meta:
        verbose_name = 'Entreprise'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
        self.__original_image = self.profilpic.name
    def save(self,*args, **kwargs):
        file_name, file_extension = os.path.splitext(self.profilpic.name)
        if self.profilpic.name != "user/pp/default.webp" and self.profilpic.name != self.__original_image:
            self.profilpic.name = str(self.uuid)+ '-' + str(int(time.time())) +  file_extension
        self.__original_image = self.profilpic.name

        if self.password != self.__original_pass and (self.is_staff == 0) :
            self.password = make_password(self.password)
            self.__original_pass = self.password
        for filenames in os.listdir('Media/user/pp'):
            if str(self.uuid) in filenames and ('user/pp/' + filenames) != self.profilpic.name:
                os.remove('Media/user/pp/'+ filenames)
        super(Entreprise, self).save(*args, **kwargs)