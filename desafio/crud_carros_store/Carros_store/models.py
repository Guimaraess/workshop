from django.db import models

# Create your models here.

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
    
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    preco = models.CharField(max_length=100)

    def __str__(self):
        return self.marca
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    numero = models.CharField(max_length=11)

    def __str__(self):
        return self.nome