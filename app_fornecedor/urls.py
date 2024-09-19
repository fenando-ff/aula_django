from django.urls import path
from . import views

#  Crie as rotas da views aqui

urlpatterns = [
    path('', views.listar_fornecedor, name='listar_fornecedor'),
    path('registrar/', views.registrar, name='registrar')
]