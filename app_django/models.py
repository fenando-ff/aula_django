from django.db import models

# Create your models here.
class USUARIO(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

# Função que mostra o nome do usuário no admin do django no lugar do 'user.object'
    def __str__(self):
        return self.nome
    










    