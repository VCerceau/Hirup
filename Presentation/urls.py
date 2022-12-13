from django.urls import path
from .views import *

urlpatterns = [
    path('<uuid:user_uuid>', index, name='index'),
]    
