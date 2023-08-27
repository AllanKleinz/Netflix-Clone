from django.forms import ModelForm
from netflixapp.models import Profile
from django import forms
from .models import Profile




class ProfileForm(ModelForm):
    
   class Meta: 
      model = Profile
      exclude = ['uuid']
    