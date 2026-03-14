from django.db import models

class Cours(models.Model):
    JOUR_CHOICES = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    enseignant = models.ForeignKey("enseignants.Enseignant", on_delete=models.CASCADE, related_name="cours")
    matiere = models.ForeignKey("matieres.Matiere", on_delete=models.CASCADE, related_name="cours")
    classe = models.ForeignKey("classes.Classe", on_delete=models.CASCADE, related_name="cours")

    jour = models.CharField(max_length=10, choices=JOUR_CHOICES ,default='Lundi')
    heure_commencer = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.matiere.nom} - {self.classe.nom} ({self.enseignant.prenom} {self.enseignant.nom}) - {self.jour}"
