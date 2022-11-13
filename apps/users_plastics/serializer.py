from rest_framework import serializers
from .models import Origin, User_Plastic

class OriginSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Origin
    fields = ('id', 'name', 'created', 'updated')
    read_only_fields = ('created', 'updated', )

class User_PlasticSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User_Plastic
    fields = ('id', 'user', 'plastic', 'origin', 'image', 'description', 'units', 'created', 'updated')