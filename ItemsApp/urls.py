from django.urls import re_path
from ItemsApp import views

urlpatterns=[
   re_path(r'^items$',views.ItemsApi),
   re_path(r'^items/([0-9]+)$',views.ItemsApi),
]