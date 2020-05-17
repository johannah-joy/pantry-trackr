from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  # password = 

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class PantryItem(models.Model):
  item = models.CharField(max_length=30)
  quantity_min = models.IntegerField()

  def __str__(self):
    return self.item
  