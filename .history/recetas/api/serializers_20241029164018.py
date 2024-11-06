from rest_framework import serializers
from ingredientes.models import Ingrediente

class IngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id_recetas','nombre_receta','descripcion','porciones','imagen']