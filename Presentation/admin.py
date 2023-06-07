from django.contrib import admin
from .models import *
# Register your models here.

class CvAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cv, CvAdmin)

class FormationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Formation, FormationAdmin)

class CompetenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Competence, CompetenceAdmin)


class CategorieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categorie, CategorieAdmin)