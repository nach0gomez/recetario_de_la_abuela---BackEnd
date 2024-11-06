from rest_framework.viewsets import ModelViewSet
from favoritos.models import Favorito
from favoritos.api.serializers import FavoritoSerializers

class FavoritoApiViewSet(ModelViewSet):
    serializer_class = FavoritoSerializers
    queryset = Favorito.objects.all()