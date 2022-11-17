from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import uuid
from Presentation.models.formation import *
from Presentation.models.cv import *
# Create your views here.

def index(request):

    return render(request, 'index.html')

def Cvs(request):
    cv = Cv.objects.all()
    formation = Formation.objects.all()
    context = {
        'cvs':cv,
        'formations': formation,
    }
    return render(request, 'cv.html', context)