from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializer import UserSerialzier

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = UserSerialzier