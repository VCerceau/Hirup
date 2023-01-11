from django.urls import path
from .views import *

urlpatterns = [
    path('<uuid:user_uuid>', index, name='cv_view'),
    path('competences_update_or_create/<uuid:comp_id>/', competences_update_or_create, name='competences_update_or_create'),
    
    
    # path('get_or_create/')
]    
