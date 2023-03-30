from rest_framework import viewsets 
from serializer import jogoSerializer
from .models import jogos
from serializer import LojaSerializer
from .models import loja

class jogoViewSet(viewset.ModelSet):
    querryset = jogos.objects.all()
    serializer_class = jogoSerializer

class lojaViewset(viewset.ModelSet):
    querryset = loja.objects.all()
    serializer_class = LojaSerializer 
