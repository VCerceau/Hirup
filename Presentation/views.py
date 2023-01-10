from django.shortcuts import render
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
    if request.method == 'GET':
        user = request.user
        user_cv = User.objects.get(uuid = user_uuid)
        personne = Personne.objects.get(uuid = user_uuid)
        context = {'user' : user,
                    'personne': personne
                    }
        context.update({'creator': (user==user_cv)})

        cv = get_or_none_with_uuid(classe=Cv, classe_uuid=User, uuid = user_uuid)
        
        if cv != None:
            context.update({'cv':cv})
            competences = filter_or_none_with_uuid(classe=Competence, classe_uuid=Cv, uuid = cv.uuid)
            for comp in competences:
                print(comp.title)
            if competences:
                context.update({'competences' : competences})

    return render(request, 'presentation/index.html', context)

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
