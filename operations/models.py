from django.db import models

# Create your models here.
class Operation(models.Model):
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=18)
    hora = models.TimeField()
    store = models.ForeignKey(
        "stores.Store", on_delete=models.CASCADE, related_name="operations"
    )
