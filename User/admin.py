from django.contrib import admin as djangoadmin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class AdminAdmin(djangoadmin.ModelAdmin):
    pass
djangoadmin.site.register(Admin, AdminAdmin)

class PersonnesAdmin(djangoadmin.ModelAdmin):
    pass
djangoadmin.site.register(Personne, PersonnesAdmin)

class EntreprisesAdmin(djangoadmin.ModelAdmin):
    pass
djangoadmin.site.register(Entreprise, EntreprisesAdmin)
