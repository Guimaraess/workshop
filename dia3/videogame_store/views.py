from rest_framework import viewsets
from .serializer import JogoSerializer
from .models import Jogos, Loja
from .serializer import LojaSerializer


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer 
