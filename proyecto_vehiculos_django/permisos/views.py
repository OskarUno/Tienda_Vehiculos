from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            
            #Asignar el grupo comun al nuevo usuario
            grupo_usuario_comun = Group.objects.get(name='Usuario_comun')
            user.groups.add(grupo_usuario_comun)
            return redirect('permisos:login')
        
    else:  # 3.8
        form = RegistroForm()
        return render(request, 'permisos/registro.html', { 'form':form })
    
    
def logout_view(request):
    # Cerrar session de usuario y redirige a la pagina de inicio
    logout(request)
    messages.success(request, 'Sesion cerrada con exito')
    return redirect('permisos:login')


def login_view(request):
    # Iniciar sesion
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'Se ha iniciado sesion con exito')
            return redirect('vehiculo:listar')
        
    else:  # 3.8
        form = AuthenticationForm()
        
    return render(request, 'permisos/login.html', {'form': form})