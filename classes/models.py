from django.db import models
from enseignants.models import Enseignant 
from matieres.models import Matiere  

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)
    annee_scolaire = models.CharField(max_length=20)
     
    def __str__(self):
        return f"{self.nom}"

class Horaire(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    temps_debut = models.TimeField()
    temps_fin = models.TimeField()
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titre} - {self.enseignant} - {self.classe} - {self.matiere.nom}'
