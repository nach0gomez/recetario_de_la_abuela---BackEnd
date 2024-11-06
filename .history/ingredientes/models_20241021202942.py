from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre_ingrediente = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'INGREDIENTES'