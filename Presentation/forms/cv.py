from django import forms
from Presentation.models import Formation, Cv

class CvForm(forms.ModelForm):
  class Meta:
    model = Cv
    fields = ['name','introduction']
    name = forms.CharField()
    introduction = forms.CharField()
    # def __init__(self, *args, **kwargs):
    #   # Get the user from the kwargs
    #   user = kwargs.pop('user')

    #   # Get the user's CV
    #   cv = Cv.objects.get_or_create(user=user)[0]

    #   # Set the cv foreign key on the form instance
    #   self.instance.cv = cv

    #   super().__init__(user ,*args, **kwargs)      