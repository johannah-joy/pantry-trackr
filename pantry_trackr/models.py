from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# this is spot on especially if no users app folder

class User(models.Model):
  # user = models.OneToOneField(User)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  # password = 

  def __str__(self):
    return self.name


class PantryItem(models.Model):
  item = models.CharField(max_length=30)
  quantity_min = models.IntegerField()

  def __str__(self):
    return self.item
  