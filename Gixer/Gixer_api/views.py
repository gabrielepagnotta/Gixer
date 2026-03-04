from rest_framework import viewsets
from .models import OreInserite
from .serializers import OreSerializer

class ore_inseriteViewSet(viewsets.ModelViewSet):
    queryset = OreInserite.objects.all()
    serializer_class = OreSerializer