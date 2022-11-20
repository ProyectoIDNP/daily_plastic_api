from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class UserTokenSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username')
