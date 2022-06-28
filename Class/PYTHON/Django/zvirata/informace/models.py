from django.db import models

# Create your models here.

class Zvire(models.Model):
    jmeno = models.CharField(max_length=100)
    barva = models.CharField(max_length=100)
    vaha = models.IntegerField(null=True, blank=True)
    popis = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"ja jsem {self.jmeno} a mam barvu {self.barva}"