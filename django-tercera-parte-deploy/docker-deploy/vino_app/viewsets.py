from rest_framework.viewsets import ModelViewSet
from .models import Vino
from .serializers import VinoSerializer

class VinoViewSet(ModelViewSet):
    queryset = Vino.objects.all()
    serializer_class = VinoSerializer