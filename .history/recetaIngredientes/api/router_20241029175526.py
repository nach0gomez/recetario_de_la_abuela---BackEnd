from rest_framework.routers import DefaultRouter
from recetaIngredientes.api.views import RecetaIngredienteApiViewSet

router_ingrediente = DefaultRouter()
router_ingrediente.register(prefix='receta_ingrediente', basename='receta_ingrediente', viewset=RecetaIngredienteApiViewSet)
