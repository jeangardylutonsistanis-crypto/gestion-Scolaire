from django import forms
from .models import Enseignant

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'contact', 'matieres']
        widgets = {
            # Montre matyè yo kòm bwat chèk pou chwazi plizyè
            'matieres': forms.CheckboxSelectMultiple(),
        }
