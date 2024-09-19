from django.shortcuts import render, redirect
from .models import USUARIO
# Create your views here.

def listar_usuarios(request):
    usuario = USUARIO.objects.all()
    return render(request, 'index.html', {'usuarios': usuario})


def salvar(request):
    n_nome = request.POST.get("nome")
    n_email = request.POST.get("email")
    n_senha = request.POST.get("senha")
    n_conf = request.POST.get("conf")
    
    if n_conf == n_senha:
        USUARIO.objects.create(nome = n_nome, email = n_email, senha = n_senha) 
        usuario = USUARIO.objects.all()
        return render(request, 'index.html', {'usuarios': usuario})
    else:
        avisos = 'As senhas não são iguais'
        return render(request, 'index.html', {'avisos': avisos})

def pegarId(request,id):
    usuarios = USUARIO.objects.get(id = id)
    return render(request, 'update.html', {'usuario': usuarios})

def update(request,id):
    n_nome = request.POST.get("nome")
    n_email = request.POST.get("email")
    n_senha = request.POST.get("senha")
    usuarios = USUARIO.objects.get(id = id)
    usuarios.nome = n_nome
    usuarios.email = n_email
    usuarios.senha = n_senha
    usuarios.save()
    return redirect(listar_usuarios)

def deletar(request,id):
    usuarios = USUARIO.objects.get(id = id)
    usuarios.delete()
    return redirect(listar_usuarios)