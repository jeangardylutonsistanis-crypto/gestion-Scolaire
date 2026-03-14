from django.db import models
from classes.models import Classe
from django.conf import settings
from django.utils import timezone



 
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.TextField()
    classe = models.ForeignKey('classes.Classe', on_delete=models.CASCADE)

 
# students/models.py

 
class Absence(models.Model):
    CHOICES = [
        ('absent', 'Absent'),
        ('present', 'Présent'),
    ]

    date = models.DateField()
    statut = models.CharField(max_length=10, choices=CHOICES, default='absent')
    etudiant = models.ForeignKey('etudiants.Etudiant', on_delete=models.CASCADE,related_name='etudiants')

    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.etudiant.nom} - {self.date} - {self.statut}"

