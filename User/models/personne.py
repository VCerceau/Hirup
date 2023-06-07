from django.db import models
from .user import *
import itertools

class Personne(User):
    firstname = models.CharField(max_length=64, null=True, blank=True)
    lastname = models.CharField(max_length=64, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Personne'
        
        
    def __str__(self):
        return f"{self.username, self.uuid}"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_pass = self.password
        self.__original_image = self.profilpic.name
        self.__original_slug = self.slug
    
    def save(self,*args, **kwargs):
        if os.path.isfile(self.get_photo_full_path()):
            os.remove(self.get_photo_full_path())
        if not self.slug or self.slug != self.__original_slug or self.firstname not in self.slug or self.lastname not in self.slug:
            self.slug = orig = slugify(self.firstname + '-' + self.lastname)
            for x in itertools.count(1):
                if not Personne.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)
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
        super(Personne, self).save(*args, **kwargs)
    @property
    def get_photo_url(self):
        return self.profilpic
    
    def get_photo_full_path(self):
        return ('/Media/') + str(self.profilpic)
    
    def mail(self):
        return self.username