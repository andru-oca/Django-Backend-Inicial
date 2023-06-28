from rest_framework import routers
from .viewsets import VinoViewSet

router = routers.SimpleRouter()
router.register("vino-api",VinoViewSet)