from rest_framework import serializers
from ingredientes.models import Ingrediente

class IngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id_ingrediente','nombre_ingrediente']