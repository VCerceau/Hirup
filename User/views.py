from django.shortcuts import render
from .models.user import User
from django.contrib.auth import logout
# Create your views here.

def login(request):

    return render(request, 'user/login.html')



def profil(request):
    return render(request, 'user/profil.html')