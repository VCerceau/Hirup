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

def index(request, user_uuid):
    if request.method == 'GET':
        
        user = request.user
        
        cv_user = User.objects.get(uuid=user_uuid)
        
        cv = Cv.objects.get(user = cv_user)
        
        competence = Competence.objects.get(cv=cv)
        
        context = {
            'user': user,
            'cv_user': cv_user,
            'cv': cv,
            'competence': competence,
        }
        return render(request, 'presentation/index.html', context)
    else:
        # Get the current user
        user = request.user

        # Get the user's CV
        cv = Cv.objects.get(user=user)
        
        competence = Competence.objects.get(cv=cv)
        uuid_comp = competence['uuid']  
        # Create a form instance with the submitted data
        form_experience = ExperienceForm(request.POST)

        # Validate the form
        if form_experience.is_valid():
            # Get the skill data from the form
            title = form_experience.cleaned_data['title']
            description = form_experience.cleaned_data['description']

            # Create a new skill for the user's CV
            competence = competence.objects.update_or_create(uuid=uuid_comp ,cv=cv, title=title, description=description)
            competence.save()
            # Do something with the new skill...

        else:
            # Create an empty form
            form_experience = ExperienceForm()

        context = {
            'form_experience': form_experience,
        }

        return render(request, 'presentation/index.html', context)

