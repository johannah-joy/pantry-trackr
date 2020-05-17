from rest_framework import serializers
from pantry_trackr import models


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'name',
      'email',
      'password',
    )
    model = models.User