# gym_app/forms.py

from django import forms
from .models import Cliente, Pago, Gasto

# Formulario Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'correo_electronico', 'pagado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
            'pagado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formulario Pago
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['cliente', 'importe']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'importe': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Importe'}),
        }

# Formulario Gasto
class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto'}),
        }
