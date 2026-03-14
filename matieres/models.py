from django.db import models
 

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
     
    def __str__(self):
        return self.nom


    def __str__(self):
        return f"{self.nom}"