from rest_framework import serializers
from pantry_trackr import models


# class UserRegisterSerializer(serializers.ModelSerializer):
#   class Meta:
#     fields = (
#       'id',
#       'username',
#     #   'password',
#       'password1',
#       'password2',
#     )
#     model = models.UserRegister

class PantryItemSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'item',
      'quantity_min',
    )
    model = models.PantryItem