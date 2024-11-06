from rest_framework import serializers
from favoritos.models import Favorito

class FavoritoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['id_favorito','comensales','user', 'id_recetas']