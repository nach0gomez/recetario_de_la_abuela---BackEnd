from rest_framework.routers import DefaultRouter
from ingredientes.api.views import IngredienteApiViewSet

router_ingrediente = DefaultRouter()
router_ingrediente.register(prefix='ingredientes', basename='ingredientes' viewset=IngredienteApiViewSet)
