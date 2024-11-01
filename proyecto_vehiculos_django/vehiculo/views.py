from django.shortcuts import render
from .models import Vehiculo

def index(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/index.html', {'vehiculos': vehiculos})

