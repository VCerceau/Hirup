from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import uuid
from django.contrib.auth.decorators import login_required

from Presentation.models.formation import *
from Presentation.models.cv import *
from .forms import ExperienceForm, ExperienceForm, FormationForm, CvForm
from .models import Competence, Experience, Cv
from User.forms import UserForm
from uuid import UUID
from User.models import User

# Create your views here.

def index(request, user_uuid):
  user = request.user
  user_cv = User.objects.get(uuid = user_uuid)
  context = {'user' : user,
              'user_cv': user_cv
              }
  context.update({'creator': (user==user_cv)})

  cv = get_or_none_with_uuid(classe=Cv, classe_uuid=User, uuid = user_uuid)
  
  if cv != None:
      context.update({'cv':cv})
      competences = filter_or_none_with_uuid(classe=Competence, classe_uuid=Cv, uuid = cv.uuid)
      if competences:
          context.update({'competences' : competences})
  return render(request, 'presentation/index.html', context)

def competences_update_or_create(request, comp_id):
  if request.method == 'POST':
    title = request.POST["title"]
    desc = request.POST["desc"]
    # comp = Competence.objects.get_or_create(uuid=comp_id)
    # print(comp)
    try:
      comp = Competence.objects.get(uuid=comp_id)
      comp.title = title
      print(desc)
      comp.description = desc
      print(comp.description)
      comp.save()
    except Competence.DoesNotExist:
      comp = Competence.objects.create(title=title, description=desc)
      comp.save()
  return redirect(index, request.user.uuid)

def create_object(classe, **kwargs):
    classe(**kwargs).save()
    

def get_or_none_with_uuid(classe, classe_uuid, uuid):
  try:
    # Récupère l'objet de classe_uuid qui a l'uuid spécifié
    classe_obj = classe_uuid.objects.get(uuid=uuid)

    # Récupère l'objet de la classe spécifiée qui a l'objet de classe_uuid spécifié en tant que foreign key
    # Utilise le nom de classe en minuscules comme nom de champ
    field_name = classe_uuid.__name__.lower()
    obj = classe.objects.get(**{field_name: classe_obj})
  except classe_uuid.DoesNotExist:
    return None
  except classe.DoesNotExist:
    return None
  
  return obj

def filter_or_none_with_uuid(classe, classe_uuid, uuid):
  try:
    # Récupère l'objet de classe_uuid qui a l'uuid spécifié
    classe_obj = classe_uuid.objects.get(uuid=uuid)

    # Récupère l'objet de la classe spécifiée qui a l'objet de classe_uuid spécifié en tant que foreign key
    # Utilise le nom de classe en minuscules comme nom de champ
    field_name = classe_uuid.__name__.lower()
    obj = classe.objects.filter(**{field_name: classe_obj})
  except classe_uuid.DoesNotExist:
    return None
  except classe.DoesNotExist:
    return None
  
  return obj
