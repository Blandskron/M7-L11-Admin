from django.db import models

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
