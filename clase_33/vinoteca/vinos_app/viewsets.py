from rest_framework.viewsets import ModelViewSet
from .serializers import VinoSerializer
from .models import Vino

class VinoViewSet(ModelViewSet):
    queryset=Vino.objects.all()
    serializer_class = VinoSerializer