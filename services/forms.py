from django import forms
from .models import Traiteur

class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = ['nom_complet', 'specialites', 'description', 
                  'adresse', 'email', 'telephone', 'image']