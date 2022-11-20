from .models import Origin, User_Plastic
from rest_framework import viewsets, permissions
from .serializer import OriginSerialzier, User_PlasticSerialzier

class OriginViewSet(viewsets.ModelViewSet):
  queryset = Origin.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = OriginSerialzier

class User_PlasticViewSet(viewsets.ModelViewSet):
  queryset = User_Plastic.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = User_PlasticSerialzier