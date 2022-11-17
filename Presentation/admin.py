from django.contrib import admin
from .models import *
# Register your models here.

class CvAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cv, CvAdmin)

class FormationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Formation, FormationAdmin)

class CompetencesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Competences, CompetencesAdmin)

class IntroductionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Introduction, IntroductionAdmin)

class CategorieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categorie, CategorieAdmin)