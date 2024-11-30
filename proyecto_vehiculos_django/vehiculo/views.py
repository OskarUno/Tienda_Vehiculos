from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect
from .forms import VehiculoForm
from .models import Vehiculo

def listar(request):
    vehiculos = Vehiculo.objects.all()
    filtro = []
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            filtro.append('bajo')
        elif vehiculo.precio >= 10000 and vehiculo.precio < 30000:
            filtro.append('medio')
        elif vehiculo.precio >= 30000:
            filtro.append('alto')    
        else:
            filtro.append('error')    
    filtro_listo = zip(vehiculos, filtro)  
    print(filtro)  
    return render(request, 'vehiculo/listar.html', {'filtro_listo': filtro_listo})    
        


#@login_required()
#@permission_required('vehiculo.view_vehiculos', raise_exception=True)
#@permission_required('vehiculo.add_vehiculos', raise_exception=True)
def add(request):
    if request.method == 'POST':
        forms = VehiculoForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('vehiculo:listar')
        
    else:  # "__latest__"
        forms = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'forms': forms })
    