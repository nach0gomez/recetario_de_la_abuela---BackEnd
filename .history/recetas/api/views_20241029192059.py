from rest_framework.viewsets import ModelViewSet
from recetas.models import Receta
from recetas.api.serializers import RecetaSerializers
from recetas.api.permissions import IsAdminReadOnly


class RecetaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = RecetaSerializers
    queryset = Receta.objects.all()