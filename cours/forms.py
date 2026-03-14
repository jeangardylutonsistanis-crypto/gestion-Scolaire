from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['enseignant', 'matiere', 'classe', 'jour', 'heure_commencer', 'heure_fin']
        widgets = {
            'jour': forms.Select(attrs={'class': 'form-control'}),
            'heure_commencer': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
