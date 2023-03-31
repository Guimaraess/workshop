
from django.contrib import admin
from django.urls import path , include
from videogame_store.views import JogoViewSet, LojaViewSet, ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos', JogoViewSet, basename='Jogo')
router.register('lojas', LojaViewSet, basename='loja')
router.register('clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
