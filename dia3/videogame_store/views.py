from rest_framework import viewsets
from .serializer import JogoSerializer, LojaSerializer, ClienteSerializer
from .models import Jogos, Loja, Cliente
class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer 

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
