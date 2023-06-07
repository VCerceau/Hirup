from django.urls import path
from .views import *

urlpatterns = [
    path('<uuid:user_uuid>', index, name='cv_view'),
    path('cv_form/<uuid:cv_uuid>', cv_form, name='cv_form'),
    path('experiences_form/<uuid:cv_uuid>', experiences_form, name='experiences_form'),
    path('competences_form/<uuid:cv_uuid>', competences_form, name='competences_form'),
    path('formation_form/<uuid:cv_uuid>', formation_form, name='formation_form'),
    path('formation_form/<uuid:cv_uuid>', formation_form, name='formation_form'),
    path('search/', search_cv, name='search_cv'),
    path('update_cv/', update_cv, name='update_cv'),
    
    
    # path('get_or_create/')
]    
