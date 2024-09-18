from django.urls import path
from . import views

#  Crie as rotas da views aqui

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios')
]