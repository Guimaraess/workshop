from django.contrib import admin
from .models import Carro, Loja, Cliente

# Register your models here.

class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco')

admin.site.register(Carro, CarroAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'numero')

admin.site.register(Cliente, ClienteAdmin)
