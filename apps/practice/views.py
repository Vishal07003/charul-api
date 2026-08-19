from rest_framework import viewsets
from .models import Practice
from .serializers import PracticeSerializer

class PracticeViewSet(viewsets.ModelViewSet):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer