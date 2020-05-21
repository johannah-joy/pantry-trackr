from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# this is spot on, especially if no users app folder

# class User(models.Model):
#   # user = models.OneToOneField(User)
#   name = models.CharField(max_length=50)
#   password1 = forms.CharField(widget=forms.PasswordInput())
#   password2 = forms.CharField(widget=forms.PasswordInput())

#   def __str__(self):
#     return self.name

# class UserRegister(UserCreationForm):

#   class Meta:
#     model = User
#     fields = ('username', 'password1', 'password2')

  # def __str__(self):
  #   return self.username
  


class PantryItem(models.Model):
  item = models.CharField(max_length=30)
  quantity_min = models.IntegerField()

  def __str__(self):
    return f'{self.item}, {self.quantity_min}'
  