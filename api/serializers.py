from rest_framework import serializers
from pantry_trackr import models


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'username',
      'email',
      'password',
    )
    model = models.User

class PantryItemSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'item',
      'quantity_min',
    )
    model = models.PantryItem