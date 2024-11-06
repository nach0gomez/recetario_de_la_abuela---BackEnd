from rest_framework.viewsets import ModelViewSet
from favoritos.models import Favorito
from favoritos.api.serializers import FavoritoSerializers
from favoritos.api.permissions import IsAdminReadOnly

class FavoritoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = FavoritoSerializers
    queryset = Favorito.objects.all()