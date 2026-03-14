from django import forms
from .models import Classe

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'niveau', 'annee_scolaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control border rounded p-2 w-full',
                'placeholder': 'Nom de la classe'
            }),
            'niveau': forms.TextInput(attrs={
                'class': 'form-control border rounded p-2 w-full',
                'placeholder': 'Niveau (Ex: 3ème, Terminale...)'
            }),
            'annee_scolaire': forms.TextInput(attrs={
                'class': 'form-control border rounded p-2 w-full',
                'placeholder': 'Année scolaire (Ex: 2024-2025)'
            }),
             
        }
