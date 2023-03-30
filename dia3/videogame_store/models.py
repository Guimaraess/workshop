from django.db import models

# Create your models here.

class jogos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome

class loja(models.Model):
        nome = models.CharField(max_length=100)
        esdereco = models.CharField(max_length=100)
        telefone = models.CharField(max_length=100)

        def __str__(self):
             return self.nome
