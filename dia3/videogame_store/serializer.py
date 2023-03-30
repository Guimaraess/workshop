from rest_framework import serializers
from .models import Jogos, Loja

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos 
        fields = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']
