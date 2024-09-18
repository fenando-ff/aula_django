from django.shortcuts import render
from .models import USUARIO
# Create your views here.

def listar_usuarios(request):
    usuario = USUARIO.objects.all()
    return render(request, 'index.html', {'usuarios': usuario})


def salvar(request):
    n_nome = request.POST.get("nome")
    n_email = request.POST.get("email")
    n_senha = request.POST.get("senha")
    USUARIO.objects.create(nome = n_nome, email = n_email, senha = n_senha)
    usuario = USUARIO.objects.all()
    return render(request, 'index.html', {'usuarios': usuario})