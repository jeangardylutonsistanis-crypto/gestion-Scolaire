from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    
    # ManyToManyField ak Matiere nan yon lòt app
    matieres = models.ManyToManyField("matieres.Matiere", related_name="enseignants", blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    # Lis matyè yo kòm string
    def get_matieres(self):
        return ", ".join([m.nom for m in self.matieres.all()])
