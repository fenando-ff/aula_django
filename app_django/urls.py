from django.urls import path
from . import views

#  Crie as rotas da views aqui

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('salvar/', views.salvar, name='salvar'),
    path('editar/<int:id>', views.pegarId, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.deletar, name='delete')
]