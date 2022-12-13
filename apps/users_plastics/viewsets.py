from .models import Origin, User_Plastic
from rest_framework import viewsets, permissions, response
from .serializer import OriginSerialzier, User_PlasticSerialzier, ConsumptionListSerialzier
from django.shortcuts import get_object_or_404

class OriginViewSet(viewsets.ModelViewSet):
  queryset = Origin.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = OriginSerialzier

class User_PlasticViewSet(viewsets.ModelViewSet):
  queryset = User_Plastic.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = User_PlasticSerialzier

  def list(self, request):
    user = request.query_params.get('user')
    queryset = User_Plastic.objects.all()
    if user is not None:
      queryset = queryset.filter(user=user)
    serializer = ConsumptionListSerialzier(queryset, many=True)
    return response.Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = User_Plastic.objects.all()
    plastic = get_object_or_404(queryset, pk=pk)
    serializer = ConsumptionListSerialzier(plastic)
    return response.Response(serializer.data)