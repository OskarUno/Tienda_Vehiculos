from django.urls import path
from . import views

app_name = 'permisos'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('cerrar_session/', views.logout_view, name='cerrar_session'),
    path('iniciar_sesion/', views.login_view, name='login'),
    path('pagina_de_error/', views.pagina_de_error, name='pagina_de_error')
]