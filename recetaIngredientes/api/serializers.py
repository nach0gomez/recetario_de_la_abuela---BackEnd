from rest_framework import serializers
from recetaIngredientes.models import RecetaIngrediente

class RecetaIngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngrediente
        fields = ['id_receta_ingredientes','id_recetas','id_ingredientes','cantidades']