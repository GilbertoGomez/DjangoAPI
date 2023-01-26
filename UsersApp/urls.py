from django.urls import re_path
from UsersApp import views

urlpatterns=[
   re_path(r'^usuarios$',views.UsuariosApi),
   re_path(r'^usuarios/([0-9]+)$',views.UsuariosApi),
]