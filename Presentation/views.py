from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import uuid
from django.contrib.auth.decorators import login_required

from Presentation.models.formation import *
from Presentation.models.cv import *
from .forms import ExperienceForm, CompetenceForm, FormationForm, CvForm, CVSearchForm
from .models import Competence, Experience, Cv
from User.forms import UserForm
from uuid import UUID
from User.models import User
from django.forms import formset_factory


# Create your views here.

def index():
    pass

def search_cv(request):
    form = CVSearchForm()

    if request.method == 'POST':
        form = CVSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cvs_w_name = Cv.objects.filter(name__icontains=query)
            cvs_w_intro = Cv.objects.filter(introduction__icontains=query)
            cvs = cvs_w_name | cvs_w_intro
            return render(request, 'presentation/search_results.html', {'cvs': cvs, 'query': query})

    return render(request, 'presentation/search_cv.html', {'form': form})

def update_cv(request):
    user_cv = request.user
    context = {'user_cv': user_cv,
               }
    context.update({'creator': (user_cv == request.user)})
    cv = get_or_none_with_uuid(classe=Cv, classe_uuid=User, uuid=user_cv.uuid)
    
    
        
    
    if cv == None:
        context.update({'cvform': cvform})
        return render(request, 'presentation/index.html', context)
    
    cv_data = {
        'name': cv.name,
        'introduction': cv.introduction
    }
    cvform=CvForm(initial=cv_data)
    
    if request.method == 'POST':
        cvform = CvForm(request.POST)
        if cvform.is_valid():
            name = cvform.cleaned_data['name']
            introduction = cvform.cleaned_data['introduction']
            obj = Cv.objects.get_or_create(user=request.user.personne)[0]
            obj.name = name
            obj.introduction = introduction
            obj.save()
            context.update({'cvform': cvform})
            context.update({'cv': cv})


    #Compétences
    competences = Competence.objects.filter(cv=cv)
    CompetenceFormSet = formset_factory(CompetenceForm, extra=1)
    competence_data = [{'title': competence.title, 'description': competence.description} for competence in competences]
    competence_formset = CompetenceFormSet(prefix='competence', initial=competence_data)
    context.update({'competences': competences, 'competenceformset':competence_formset})
    
    #Experiences
    experiences = Experience.objects.filter(cv=cv)
    ExperienceFormSet = formset_factory(ExperienceForm, extra=1)
    experience_data = [{'title': experience.title, 'description': experience.description} for experience in experiences]
    experience_formset = ExperienceFormSet(prefix='experience', initial=experience_data)
    context.update({'experiences': experiences, 'experienceformset':experience_formset})
    
    #Formations
    formations = Formation.objects.filter(cv=cv)
    FormationFormSet = formset_factory(FormationForm, extra=1)
    formation_data = [{'title': formation.title, 'description': formation.description, 'mention': formation.mention} for formation in formations]
    formation_formset = FormationFormSet(prefix='formation', initial=formation_data)
    context.update({'formations': formations, 'formationformset':formation_formset})
    
    

    

    context.update({'cvform': cvform})
    context.update({'cv': cv})     
    
    return render(request, 'presentation/index.html', context)

def cv_form(request, cv_uuid):
    user = request.user
    cv = Cv.objects.get(uuid=cv_uuid)
    cv_owner = cv.user
    
    formations = Formation.objects.filter(cv=cv)
    experiences = Experience.objects.filter(cv=cv)
    competences = Competence.objects.filter(cv=cv)
    context = {'user': user,
                   'cv': cv,
                   'cv_owner': cv_owner,
                   'experiences': experiences,
                   'formations': formations,
                   'competences': competences,
               }
    return render(request, 'presentation/show_cv.html', context)

def competences_form(request, cv_uuid):
    CompetenceFormSet = formset_factory(CompetenceForm)
    competences = Competence.objects.filter(cv=Cv.objects.get(uuid=cv_uuid))
    competence_data = [{'title': competence.title, 'description': competence.description} for competence in competences]
    competence_formset = CompetenceFormSet(request.POST, prefix='competence', initial=competence_data)
    if competence_formset.is_valid():
        counter = 0
        for competence_form  in competence_formset:
            if competence_form.cleaned_data:
                title = competence_form.cleaned_data['title']
                description = competence_form.cleaned_data['description']
                obj = Competence.objects.get_or_create(order=counter, cv=Cv.objects.get(uuid=cv_uuid))[0]
                obj.title = title
                obj.description = description
                obj.save()
                counter += 1
    return redirect('update_cv')

def experiences_form(request, cv_uuid):
    ExperienceFormSet = formset_factory(ExperienceForm)
    if request.method != 'POST':
        experience_formset = ExperienceFormSet(prefix='experience')
    experiences = Experience.objects.filter(cv=Cv.objects.get(uuid=cv_uuid))
    experience_data = [{'title': experience.title, 'description': experience.description} for experience in experiences]
    experience_formset = ExperienceFormSet(request.POST, prefix='experience', initial=experience_data)
    if experience_formset.is_valid():
        counter = 0
        for experience_form  in experience_formset:
            if experience_form.cleaned_data:
                title = experience_form.cleaned_data['title']
                description = experience_form.cleaned_data['description']
                obj = Experience.objects.get_or_create(order=counter, cv=Cv.objects.get(uuid=cv_uuid))[0]
                obj.title = title
                obj.description = description
                obj.save()
                counter += 1
    return redirect('update_cv')

def formation_form(request, cv_uuid):
    FormationFormSet = formset_factory(FormationForm)
    if request.method != 'POST':
        formation_formset = FormationFormSet(prefix='formation')
    formations = Formation.objects.filter(cv=Cv.objects.get(uuid=cv_uuid))
    formation_data = [{'title': formation.title, 'description': formation.description, 'mention': formation.mention} for formation in formations]
    formation_formset = FormationFormSet(request.POST, prefix='formation', initial=formation_data)
    if formation_formset.is_valid():
        counter = 0
        for formation_form  in formation_formset:
            if formation_form.cleaned_data:
                title = formation_form.cleaned_data['title']
                description = formation_form.cleaned_data['description']
                # mention = formation_form.cleaned_data['mention']
                obj = Formation.objects.get_or_create(order=counter, cv=Cv.objects.get(uuid=cv_uuid))[0]
                obj.title = title
                obj.description = description
                # obj.mention = mention
                obj.save()
                counter += 1
    else:
        print(formation_formset)
    return redirect('update_cv')


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

        return obj
    except classe_uuid.DoesNotExist:
        return None
    except classe.DoesNotExist:
        return None
