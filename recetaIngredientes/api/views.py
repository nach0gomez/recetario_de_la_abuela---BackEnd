from rest_framework.viewsets import ModelViewSet
from recetaIngredientes.models import RecetaIngrediente
from recetaIngredientes.api.serializers import RecetaIngredienteSerializers
from recetaIngredientes.api.permissions import IsAdminReadOnly

class RecetaIngredienteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = RecetaIngredienteSerializers
    queryset = RecetaIngrediente.objects.all()