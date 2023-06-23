from rest_framework.serializers import ModelSerializer 
from .models import Vino

class VinoSerializer(ModelSerializer):
    class Meta:
        model = Vino
        fields= '__all__'
