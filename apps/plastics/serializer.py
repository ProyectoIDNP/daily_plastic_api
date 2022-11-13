from rest_framework import serializers
from .models import Category, Presentation, Plastic

class CategorySerialzier(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'created', 'updated')
    read_only_fields = ('created', 'updated', )

class PresentationSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Presentation
    fields = ('id', 'name', 'created', 'updated')
    read_only_fields = ('created', 'updated', )

class PlasticSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Plastic
    fields = ('id', 'category', 'presentation', 'name', 'decomposition_time', 'unit_weight', 'created', 'updated')