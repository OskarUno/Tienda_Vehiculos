from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:  # Clase Meta define campos dentro del formulario
        model = User
        fields = ['username', 'email', 'password']