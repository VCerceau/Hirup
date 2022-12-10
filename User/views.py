from django.shortcuts import render
from User.models.personne import Personne
from User.models.user import User
from django.contrib.auth import logout
from django import forms
from User.forms import EditProfileForm
# Create your views here.

def login(request):

    return render(request, 'user/login.html')



def profil(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire soumis
        form = EditProfileForm(request.POST)

        # Vérifier si le formulaire est valide
        if form.is_valid():
            # Enregistrer les données du formulaire en utilisant l'utilisateur actuel
            form.save(personne=request.personne)
            # Afficher un message de succès ou rediriger vers une autre page ici
    else:
        # Récupérer les données de l'utilisateur actuel pour préremplir le formulaire
        initial_data = {
            'email': request.user.email,
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'phonenumber': request.user.phonenumber,
            'adress': request.user.adress,
            'profilpic': request.user.profilpic,
        }
        form = EditProfileForm(initial=initial_data)

    return render(request, 'user/profil.html', {'form': form})