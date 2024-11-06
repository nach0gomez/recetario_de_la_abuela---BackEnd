from rest_framework.viewsets import ModelViewSet
from recetas.models import Receta
from recetas.api.serializers import RecetaSerializers

class RecetaApiViewSet(ModelViewSet):
    serializer_class = RecetaSerializers
    queryset = Receta.objects.all()