from re import U
from rest_framework import viewsets
from ecommerce.models import *
from ecommerce.serializer import *


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
