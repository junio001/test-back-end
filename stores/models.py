
from django.db import models

# Create your models here.
class Store(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    dono = models.CharField(max_length=128)