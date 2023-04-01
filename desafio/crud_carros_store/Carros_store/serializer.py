from rest_framework import serializers
from .models import Carro, Loja, Cliente

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'preco']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'numero']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']
