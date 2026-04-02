from django.db import models
from django.utils import timezone 

class Traiteur(models.Model):
    nom_complet = models.CharField(max_length=255)
    specialites = models.CharField(max_length=255)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=True)
    email = models.EmailField()
    date_de_creation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='', blank=True, null=True) 

    def __str__(self):
        return self.nom_complet
