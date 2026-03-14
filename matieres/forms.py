from django import forms
# from enseignants.models import Enseignant
from .models import Matiere

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom']
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Kòd ou ap itilize 'Enseignant' la pral kounye a rekonèt
    #     self.fields['enseignant'].queryset = Enseignant.objects.all()  # Customize queryset if needed
