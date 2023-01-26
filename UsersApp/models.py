from django.db import models

# Create your models here.
class Usuarios(models.Model):
   UsuarioId = models.AutoField(primary_key=True)
   UsuariosNombre = models.CharField(max_length=100)