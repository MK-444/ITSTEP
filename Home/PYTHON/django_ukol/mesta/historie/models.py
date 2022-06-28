from django.db import models

# Create your models here.

class City(models.Model):
    nazev = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pocasi  = models.CharField(max_length=100)
    doprava = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Nazev mesta {self.nazev} je {self.pocasi}"