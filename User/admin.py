from django.contrib import admin as djangoadmin
from .models import *
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
