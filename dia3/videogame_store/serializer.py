from rest_framework import serializers
from .models import jogo, Loja

class jogoSerializer(serializers.ModelSerializer):
    class meta:
        model = jogo 
        fildes = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class meta:
        model = Loja
        fildes = ['nome', 'endereco', 'telefone']
