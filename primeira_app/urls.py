from django.contrib import admin
from django.urls import path, include
from .views import cadastrar_usuario

urlpatterns = [
     path('', cadastrar_usuario, name='cadastrar_usuario'),
]