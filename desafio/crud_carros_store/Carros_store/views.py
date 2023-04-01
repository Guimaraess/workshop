from rest_framework import viewsets
from .serializer import CarroSerializer, LojaSerializer, ClienteSerializer
from .models import Carro, Cliente, Loja

# Create your views here.

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer





