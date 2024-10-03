# gym_app/models.py

'''
Explicación:

Cliente: Almacena la información personal del cliente (nombre, apellido, teléfono, etc.).
Pago: Registra si un cliente ha pagado el mes correspondiente. Asociado al cliente con un ForeignKey.
Gasto: Para registrar los gastos del gimnasio en un mes dado.
'''

from django.db import models
from django.utils import timezone
import datetime

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(blank=True, null=True)
    pagado = models.BooleanField(default=False)
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mes = models.DateField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pago de {self.cliente.nombre} {self.cliente.apellido} - {self.mes.strftime('%B %Y')}"

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion
