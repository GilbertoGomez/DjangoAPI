from rest_framework import serializers
from UsersApp.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields=('UsuarioId','UsuariosNombre')
