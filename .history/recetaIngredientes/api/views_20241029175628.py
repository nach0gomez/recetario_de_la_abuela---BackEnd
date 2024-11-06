from rest_framework.viewsets import ModelViewSet
from recetaIngredientes.models import RecetaIngrediente
from recetaIngredientes.api.serializers import RecetaIngredienteSerializers

class RecetaIngredienteApiViewSet(ModelViewSet):
    serializer_class = RecetaIngredienteSerializers
    queryset = RecetaIngrediente.objects.all()