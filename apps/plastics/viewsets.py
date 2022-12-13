from .models import Category, Presentation, Plastic
from rest_framework import viewsets, permissions, response
from .serializer import CategorySerialzier, PresentationSerialzier, PlasticSerialzier, PlasticListSerialzier
from django.shortcuts import get_object_or_404

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

  def list(self, request):
    queryset = Plastic.objects.all()
    serializer = PlasticListSerialzier(queryset, many=True)
    return response.Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = Plastic.objects.all()
    plastic = get_object_or_404(queryset, pk=pk)
    serializer = PlasticListSerialzier(plastic)
    return response.Response(serializer.data)