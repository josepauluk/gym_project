# gym_app/forms.py

from django import forms
from .models import Cliente, Pago, Gasto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'correo_electronico']

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['cliente', 'importe', 'mes']  # Asegúrate de que 'cliente' está incluido

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'fecha']
