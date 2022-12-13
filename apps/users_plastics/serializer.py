from rest_framework import serializers
from .models import Origin, User_Plastic
from ..plastics.serializer import PlasticListSerialzier

class OriginSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Origin
    fields = ('id', 'name',)

class User_PlasticSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User_Plastic
    fields = ('id', 'user', 'plastic', 'origin', 'image', 'description', 'units', 'updated')

class ConsumptionListSerialzier(serializers.ModelSerializer):
  origin = OriginSerialzier()
  plastic = PlasticListSerialzier()

  class Meta:
    model = User_Plastic
    fields = ('id', 'user', 'plastic', 'origin', 'image', 'description', 'units', 'updated')