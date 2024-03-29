from django import forms
from Presentation.models import Competence, Cv

class CompetenceForm(forms.ModelForm):
  class Meta:
    model = Competence
    fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
      # Get the user from the kwargs
      user = kwargs.pop('user')

      # Get the user's CV
      cv = Cv.objects.get(user=user)

      # Set the cv foreign key on the form instance
      self.instance.cv = cv

      super().__init__(*args, **kwargs)