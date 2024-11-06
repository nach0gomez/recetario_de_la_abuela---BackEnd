from rest_framework.viewsets import ModelViewSet
from ingredientes.models import Ingrediente
from ingredientes.api.serializers import IngredienteSerializer

class IngredienteApiViewSet(ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()