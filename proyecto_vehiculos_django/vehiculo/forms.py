from django import forms
from .models import Vehiculo

MARCAS = [ ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'), ] 
CATEGORIAS = [ ('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga'), ]

class VehiculoForm(forms.ModelForm):
    marca = forms.ChoiceField(choices = MARCAS)
    modelo = forms.CharField(max_length=100)
    serial_carroceria = forms.CharField(max_length=50) 
    serial_motor = forms.CharField(max_length=50) 
    categoria = forms.ChoiceField(choices = CATEGORIAS) 
    precio = forms.DecimalField(max_digits=10, decimal_places=2) 

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria','serial_motor','categoria', 'precio']
    