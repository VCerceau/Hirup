from django.contrib import admin
from .models import *
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categorie, CategorieAdmin)
