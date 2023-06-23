from rest_framework import routers
from .viewsets import VinoViewSet

# nos permite tener algo más controlado y le da las rutas dependiendo del viewset


router = routers.SimpleRouter()
router.register('vino',VinoViewSet)