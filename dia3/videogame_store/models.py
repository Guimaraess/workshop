from django.db import models

# Create your models here.

class Jogos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome

class Loja(models.Model):
        nome = models.CharField(max_length=100)
        endereco = models.CharField(max_length=100)
        telefone = models.CharField(max_length=100)

        def __str__(self):
             return self.nome
        
class Cliente(models.Model):
     nome = models.CharField(max_length=100)
     cpf = models.CharField(max_length=11)
     numero = models.CharField(max_length=11)

     def __str__(self):
          return self.nome
