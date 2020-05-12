from django.db import models

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=254)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class PantryItem(models.Model):
  item = models.CharField(max_length=30)
  quantity_min = models.IntegerField()

  def __str__(self):
      return self.item
  