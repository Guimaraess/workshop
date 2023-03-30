from django.contrib import admin
from .models import Jogos, Loja

# Register your models here.

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Jogos, JogosAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)
