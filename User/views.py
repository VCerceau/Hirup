from django.shortcuts import render
from User.models.personne import Personne
from User.models.user import User
from django.contrib.auth import logout
from django import forms
from User.forms import EditProfileForm
# Create your views here.

def login(request):

    return render(request, 'user/login.html')

def index(request):
    user = request.user
    
    return render(request, 'index.html', {'user': user})

def profil(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire soumis
        form = EditProfileForm(request.POST)

        # Vérifier si le formulaire est valide
        if form.is_valid():
            form.save(user=request.user.personne)
            # Enregistrer les données du formulaire en utilisant l'utilisateur actuel
            # Afficher un message de succès ou rediriger vers une autre page ici
    else:
        # Récupérer les données de l'utilisateur actuel pour préremplir le formulaire
        initial_data = {
            'profilpic': request.user.profilpic,
            'email': request.user.username,
            'firstname': request.user.personne.firstname,
            'lastname': request.user.personne.lastname,
            'phonenumber': request.user.phonenumber,
            'adresse': request.user.adresse,
        }
        form = EditProfileForm(initial=initial_data)

    return render(request, 'user/profil.html', {'form': form})