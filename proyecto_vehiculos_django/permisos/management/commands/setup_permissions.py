from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from vehiculo.models import Vehiculo

#Comnand se usa para crear comandos personalizados
class Command(BaseCommand):
    help = "Configura el usuario Admin y los grupos de permisos y los permisos iniciales"

    def handle(self, *args, **kwargs):
        #Crea el usuario admin con permisos completos
        admin_user, created = User.objects.get_or_create(
            username = 'admin', 
            defaults={'email':'admin@gmail.com', 'is_staff':True, 'is_superuser':True})
        
        if created:
            admin_user.set_password('admin')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Usuario creado con exito'))
            
        else:  # 3.8
            self.stdout.write(self.style.WARNING('Usuario ya existe'))
            
        #Crear grupos de usuarios
        grupo_permisos = {
            'Usuario_comun' : ['view_vehiculo'],
            'Editor'        : ['view_vehiculo','add_vehiculo'],
        }
        
        content_type = ContentType.objects.get_for_model(Vehiculo)
        
        for grupo_nombre, permisos in grupo_permisos.items():
            grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
            
            for permiso_codename in permisos:
                try:
                    permiso = Permission.objects.get(
                        codename=permiso_codename,
                        content_type=content_type
                    )
                    
                except Permission.DoesNotExist:
                    permiso, _ = Permission.objects.create(
                        codename=permiso_codename,
                        name=f'Can {permiso_codename} vehiculo',
                        content_type=content_type
                    )
                grupo.permissions.add(permiso)
                print(permiso)
            
        #Mensajes de ok o advertencia   
            if creado:
                self.stdout.write(self.style.SUCCESS(f'Grupo {grupo_nombre} creado y permisos asignados con exito.'))
            
            else:  # 3.8
                self.stdout.write(self.style.WARNING(f'Grupo {grupo_nombre} ya existe'))
            
        #Asignar el grupo editor al usuario admin y darle todos los permisos
        editor_group = Group.objects.get(name='Editor')
        admin_user.groups.add(editor_group)
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        self.stdout.write(self.style.SUCCESS('Configuracion inicial completada'))
