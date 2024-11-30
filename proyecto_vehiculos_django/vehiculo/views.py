from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect
from .forms import VehiculoForm
from .models import Vehiculo

def index(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/index.html', {'vehiculo': vehiculos})


#@login_required()
#@permission_required('vehiculo.view_vehiculos', raise_exception=True)
#@permission_required('vehiculo.add_vehiculos', raise_exception=True)
def add(request):
    if request.method == 'POST':
        forms = VehiculoForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('vehiculo:index')
        
    else:  # "__latest__"
        forms = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'forms': forms })
    