from django.contrib import admin
from .models import jogos, loja

# Register your models here.

class jogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(jogos, jogosAdmin)

class lojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(loja, lojaAdmin)
