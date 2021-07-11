from django.contrib import admin
from django.urls import path, include
from ecommerce.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'categorias', CategoriasViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'pedidos', PedidosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
