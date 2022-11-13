from .models import Category, Presentation, Plastic
from rest_framework import viewsets, permissions
from .serializer import CategorySerialzier, PresentationSerialzier, PlasticSerialzier

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = CategorySerialzier

class PresentationViewSet(viewsets.ModelViewSet):
  queryset = Presentation.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = PresentationSerialzier

class PlasticViewSet(viewsets.ModelViewSet):
  queryset = Plastic.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = PlasticSerialzier