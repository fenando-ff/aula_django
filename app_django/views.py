from django.shortcuts import render
from .models import USUARIO
# Create your views here.

def listar_usuarios(request):
    usuarios = USUARIO.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})