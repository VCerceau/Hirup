from django.shortcuts import render, get_object_or_404, redirect
from User.models.personne import Personne
from User.models.entreprise import Entreprise
from User.models.user import User
from django.contrib.auth import logout
from django import forms
from User.forms import EditProfileForm
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.decorators import login_required
from .forms.personne import EditProfileForm

from User.forms.personne import PersonneSignup
from User.forms.entreprise import EntrepriseSignup
from User.forms.user import ProfileForm
# Create your views here.

def login(request):

    return render(request, 'user/login.html')

def personnesignup(request):
    if request.method == "POST":
        form = PersonneSignup(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'user/personnesignup.html', context)
        
    else:
        form = PersonneSignup()
        context = {
            'form':form
        }
        return render(request, 'user/personnesignup.html', context)

def entreprisesignup(request):
    if request.method == "POST":
        form = EntrepriseSignup(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'user/entreprisesignup.html', context)
        
    else:
        form = EntrepriseSignup()
        context = {
            'form':form
        }
        return render(request, 'user/entreprisesignup.html', context)


def index(request):
    user = request.user
    
    return render(request, 'index.html', {'user': user})

def profil(request):
    form = None
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=user)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            if Personne.objects.get(pk=user.pk):
                personne = user.personne
                personne.firstname = request.POST['firstname']
                personne.lastname = request.POST['lastname']
                personne.save()
            elif Entreprise.objects.get(pk=user.pk):
                entreprise = user.entreprise
                entreprise.name = request.POST['name']
                entreprise.siret = request.POST['siret']
                entreprise.save()
            user.save()
        else:
            print('bbbbb')
    else:
        form = ProfileForm(instance=user)
    context = {
        'user':user,
        'form':form,
    }
    return render(request, 'user/profil.html', context)
