from rest_framework import viewsets
from django.shortcuts import render
from pantry_trackr.models import User, PantryItem
from .serializers import UserSerializer, PantryItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class DetailUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer


class PantryItemViewSet(viewsets.ModelViewSet):
    queryset = PantryItem.objects.all()
    serializer_class = PantryItemSerializer

# class DetailPantryItem(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.PantryItem.objects.all()
#     serializer_class = PantryItemSerializer