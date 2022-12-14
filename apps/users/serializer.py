from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialzier(serializers.ModelSerializer):

  def create(self, validated_data):
    user = User(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

  class Meta:
    model = User
    fields = '__all__'

class UserTokenSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username')
