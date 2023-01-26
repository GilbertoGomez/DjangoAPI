from django.db import models

# Create your models here.
class Categories(models.Model):
   id = models.AutoField(primary_key=True)
   ProductsName = models.CharField(max_length=100)
   CategoriesName = models.CharField(max_length=100)
