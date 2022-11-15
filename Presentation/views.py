from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import uuid
from Presentation.models.formation import *
# Create your views here.


def index(request):
    list = Formation.objects.all()
    context = {
        'formations': list,
    }
    return render(request, 'index.html', context)