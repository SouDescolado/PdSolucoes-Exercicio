from django.contrib import admin
from ecommerce.models import *


class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf')


class Categorias(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'total')
    list_display_links = ('id', 'total')
    search_fields = ('id',)


admin.site.register(Usuario, Usuarios)
admin.site.register(Categoria, Categorias)
admin.site.register(Produto, Produtos)
admin.site.register(Pedido, Pedidos)
