from rest_framework import viewsets
from .models import Stat
from .serializers import StatSerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer