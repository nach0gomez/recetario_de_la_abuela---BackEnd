from rest_framework import serializers
from favoritos.models import Favorito

class FavoritoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['id_favorito','comensales','id_usuario', 'id_recetas']