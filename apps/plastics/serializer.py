from rest_framework import serializers
from .models import Category, Presentation, Plastic

class CategorySerialzier(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name',)

class PresentationSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Presentation
    fields = ('id', 'name',)

class PlasticSerialzier(serializers.ModelSerializer):
  class Meta:
    model = Plastic
    fields = ('id', 'category', 'presentation', 'name', 'decomposition_time', 'unit_weight',)

class PlasticListSerialzier(serializers.ModelSerializer):
  category = CategorySerialzier()
  presentation = PresentationSerialzier()

  class Meta:
    model = Plastic
    fields = ('id', 'category', 'presentation', 'name', 'decomposition_time', 'unit_weight',)