from rest_framework import serializers
from recetaIngredientes.models import RecetaIngrediente

class RecetaIngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngrediente
        fields = ['id_ingrediente','nombre_ingrediente']