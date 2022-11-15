from django.contrib import admin
from .models import *
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categorie, CategorieAdmin)

class FormationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Formation, FormationAdmin)

class CvAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cv, CvAdmin)

class IntroductionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Introduction, IntroductionAdmin)