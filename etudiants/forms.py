from django import forms
from .models import Etudiant
from .models import Absence


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_naissance', 'adresse', 'classe']

        widgets = {
            'date_naissance': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
        }



# students/forms.py

 
class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['date', 'statut', 'etudiant', 'classe']

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
        }
