from django import forms
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):


    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria','serial_motor','categoria', 'precio']
        widgets = {
            'modelo': forms.Textarea(attrs={'rows': 1}),
            'serial_carroceria': forms.Textarea(attrs={'rows': 1}),
            'serial_motor': forms.Textarea(attrs={'rows': 1})
            }
        
        
