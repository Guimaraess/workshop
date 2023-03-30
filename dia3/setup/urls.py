
from django.contrib import admin
from django.urls import path
from videogame_store.views import jogoViewSet, lojaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos', JogoViewSet, basename='Jogos')
router.register('lojas', LojaViewSet, basename='loja')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
