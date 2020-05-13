from rest_framework import serializers
from pantry_trackr import models


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'first_name',
      'last_name',
      'email',
    )
    model = models.User