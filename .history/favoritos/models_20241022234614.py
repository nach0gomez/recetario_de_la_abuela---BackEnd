from django.db import models
from users.models import User
from recetas.models import Receta

# Create your models here.
class Favorito(models.Model):
    id_favorito = models.AutoField(db_column='id_favorito',primary_key=True)
    comensales = models.IntegerField()
    id_usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_usuario')
    id_recetas = models.ForeignKey(Receta, on_delete=models.SET_NULL, null=True, db_column='id_recetas')

    class Meta:
        managed = False
        db_table = 'FAVORITOS'