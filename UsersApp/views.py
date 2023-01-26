from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from UsersApp.models import Usuarios
from UsersApp.serializers import UsuariosSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def UsuariosApi(request,id=0):
   if request.method=='GET':
      usuarios = Usuarios.objects.all()
      usuarios_serializer=UsuariosSerializer(usuarios,many=True)
      return JsonResponse(usuarios_serializer.data,safe=False)
   elif request.method=='POST':
      usuario_data=JSONParser().parse(request)
      usuarios_serializer=UsuariosSerializer(data=usuario_data)
      if usuarios_serializer.is_valid():
         usuarios_serializer.save()
         return JsonResponse("Guardado correctamente",safe=False)
      return JsonResponse("Error no se pudo guardar",safe=False)
   elif request.method=='PUT':
      usuario_data=JSONParser().parse(request)
      usuario=Usuarios.objects.get(UsuarioId=usuario_data['UsuarioId'])
      usuarios_serializer=UsuariosSerializer(usuario,data=usuario_data)
      if usuarios_serializer.is_valid():
         usuarios_serializer.save()
         return JsonResponse("Se actualizó correctamente",safe=False)
      return JsonResponse("Error no se pudo actualizar",safe=False)
   elif request.method=='DELETE':
      usuario=Usuarios.objects.get(UsuarioId=id)
      usuario.delete()
      return JsonResponse("Eliminado correctamente",safe=False)