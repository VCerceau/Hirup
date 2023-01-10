from django.shortcuts import render
from User.models.personne import Personne
from User.models.user import User
from django.contrib.auth import logout
from django import forms
from User.forms import EditProfileForm
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your views here.

def login(request):

    return render(request, 'user/login.html')

def personnesignup(request):
    if request.method == "POST":
        
        username = request.POST["email"]
        password = make_password(request.POST["password"])
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        
        new = Personne(username=username, password=password, firstname=firstname, lastname=lastname)
        new.save()
        
        return render(request, 'user/login.html')
    else:
        return render(request, 'user/personnesignup.html')

def index(request):
    user = request.user
    
    return render(request, 'index.html', {'user': user})

def profil(request):
    if request.method == 'POST':
        pass
    else:
        context = {}
        # Récupérer les données de l'utilisateur actuel pour préremplir le formulaire
        user = User.objects.get(uuid = request.user.uuid)
        context.update({'user': user})
        

    return render(request, 'user/profil.html', context)