from django.db import models
from recetas.models import Receta
from ingredientes.models import Ingrediente

# Create your models here.
class RecetaIngrediente(models.Model):
    id_receta_ingredientes = models.AutoField(db_column='id_receta_ingredientes', primary_key=True)  # Field name made lowercase.
    id_recetas = models.ForeignKey(Receta, on_delete=models.SET_NULL, null=True, db_column='id_recetas')
    id_ingredientes = models.ForeignKey(Ingrediente, on_delete=models.SET_NULL, null=True, db_column='id_ingredientes')  # Field name made lowercase.
    cantidades = models.DecimalField(max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'RECETA-INGREDIENTES'