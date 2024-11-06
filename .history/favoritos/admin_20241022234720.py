from django.contrib import admin
from favoritos.models import Favorito

# Register your models here.
@admin.register(Favorito)

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['comensales', 'id_usuario', 'id_recetas']