from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import uuid
from Presentation.models.formation import *
from Presentation.models.cv import *
from .forms import ExperienceForm, ExperienceForm, FormationForm, CvForm
from .models import Competence, Experience, Cv
from User.forms import UserForm
from uuid import UUID
from User.models import User

# Create your views here.

def index(request):
    if request.method == 'GET':
        user = request.user
        
        cv = None
        competence = None
        error = None
        
        try:
            cv = Cv.objects.get(user = user.uuid)
            try:
                competence = Competence.objects.get(cv=cv)
            except:
                error = "Il n'y "
        except:
            Cv = None
        
        context = {
            'user': user,
            'cv': cv,
            'competence': competence,
        }
        
    return render(request, 'presentation/index.html', context)

def add_cv(request, name, description):
        return render(request, 'presentation/index.html,')
