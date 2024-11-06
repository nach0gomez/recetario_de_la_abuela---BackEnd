from rest_framework import serializers
from recetas.models import Receta

class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['id_recetas','nombre_receta','descripcion','porciones','imagen']