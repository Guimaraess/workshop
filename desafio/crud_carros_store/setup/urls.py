from Carros_store.views import CarroViewSet, ClienteViewSet, LojaViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('carros', CarroViewSet, basename='carros')
router.register('lojas', LojaViewSet, basename='lojas')
router.register('clientes', ClienteViewSet, basename='clientes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]




