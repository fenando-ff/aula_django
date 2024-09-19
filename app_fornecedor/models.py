from django.db import models

# Create your models here.
class FORNECEDOR(models.Model):
    nome_f = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=18, unique=True)
    produto = models.CharField(max_length=80)
    descricao= models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_f