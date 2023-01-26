from rest_framework import serializers
from ItemsApp.models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
   class Meta:
      model=Categories
      fields=('id','CategoriesName','ProductsName',)