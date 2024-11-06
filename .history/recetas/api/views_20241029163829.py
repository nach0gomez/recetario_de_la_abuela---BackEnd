from rest_framework.viewsets import ModelViewSet
from recetas.models import Receta
from recetas.api.serializers import RecetaSerializers

class IngredienteApiViewSet(ModelViewSet):
    serializer_class = IngredienteSerializers
    queryset = Receta.objects.all()