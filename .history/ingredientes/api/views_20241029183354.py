from rest_framework.viewsets import ModelViewSet
from ingredientes.models import Ingrediente
from ingredientes.api.serializers import IngredienteSerializers
from ingredientes.api.permissions import IsAdminReadOnly


class IngredienteApiViewSet(ModelViewSet):
    serializer_class = IngredienteSerializers
    queryset = Ingrediente.objects.all()