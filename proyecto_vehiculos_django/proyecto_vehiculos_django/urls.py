from . import views 
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculo/', include('vehiculo.urls')),
    path('permisos/', include(('permisos.urls', 'permisos'), namespace='permisos')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login')
]
