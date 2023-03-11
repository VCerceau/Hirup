from django.shortcuts import render, get_object_or_404
from User.models.personne import Personne
from User.models.user import User
from django.contrib.auth import logout
from django import forms
from User.forms import EditProfileForm
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.decorators import login_required
from .forms.personne import EditProfileForm

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


@login_required
def profil(request):
    context = {}
    # Récupérer les données de l'utilisateur actuel pour préremplir le formulaire
    personne = get_object_or_404(Personne, pk=request.user.uuid)
    context.update({'user': personne})
    if request.method == 'POST':
        form = EditProfileForm(files = request.FILES, instance=personne, data=request.POST)
        if form.is_valid():
            print(request.FILES)
            personne.profilpic = request.FILES
            form.save()
    else:
        form = EditProfileForm(instance=personne)
    context.update({'form':form})
    return render(request, 'user/profil.html', context)

def test(request):
    return render(request, 'test.html')
