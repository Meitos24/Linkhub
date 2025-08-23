from rest_framework import serializers  # type: ignore
from .models import Usuario

class UsuarioSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' # all campos del modelo 'Usuario'
