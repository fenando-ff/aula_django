from django.shortcuts import render, redirect
from .models import FORNECEDOR

# Create your views here.
def listar_fornecedor(request):
    fornecedor = FORNECEDOR.objects.all()
    return render(request, 'fornecedor.html', {'fornecedores': fornecedor})

def registrar(request):
    n_nome_f = request.POST.get('forne')
    n_cnpj = request.POST.get('cnpj')
    n_prod = request.POST.get('prod')
    n_desc = request.POST.get('desc')
    FORNECEDOR.objects.create(nome_f=n_nome_f, cnpj= n_cnpj, produto= n_prod, descricao= n_desc)
    fornecedor = FORNECEDOR.objects.all()
    return render(request, 'fornecedor.html', {'fornecedores': fornecedor})
