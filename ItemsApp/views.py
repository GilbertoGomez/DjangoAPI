from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ItemsApp.models import Categories
from ItemsApp.serializers import CategoriesSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def ItemsApi(request,id=0):
   if request.method=='GET':
      items = Categories.objects.all()
      items_serializer=CategoriesSerializer(items,many=True)
      return JsonResponse(items_serializer.data,safe=False)
   elif request.method=='POST':
      item_data=JSONParser().parse(request)
      items_serializer=CategoriesSerializer(data=item_data)
      if items_serializer.is_valid():
         items_serializer.save()
         return JsonResponse("Guardado correctamente",safe=False)
      return JsonResponse("Error no se pudo guardar",safe=False)
   elif request.method=='PUT':
      item_data=JSONParser().parse(request)
      items=Categories.objects.get(id=item_data['id'])
      items_serializer=CategoriesSerializer(items,data=item_data)
      if items_serializer.is_valid():
         items_serializer.save()
         return JsonResponse("Se actualizó correctamente",safe=False)
      return JsonResponse("Error no se pudo actualizar",safe=False)
   elif request.method=='DELETE':
      item=Categories.objects.get(id=id)
      item.delete()
      return JsonResponse("Eliminado correctamente",safe=False)